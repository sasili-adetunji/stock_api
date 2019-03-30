import os
from sqlalchemy import exc
from flask import Flask, jsonify, request, Blueprint
from project.api.models import Stocks
from project.api.utils import authenticate
from project import db

stocks_blueprint = Blueprint('stocks', __name__)

@stocks_blueprint.route('/stocks/ping', methods=['GET']) 
def stocks_pong():
    return jsonify({ 
      'status': 'success', 
      'message': 'stocks'
})

@stocks_blueprint.route('/stocks/', methods=['POST'])
@authenticate
def post_stocks(resp):
    if not resp['data']:
        response_object = {
            'status': 'error',
            'message': 'You do not have permission to do that.'
        }
        return jsonify(response_object), 401

    # get post data
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    if not post_data:
        return jsonify(response_object), 400

    stock_name = post_data.get('stock_name')
    opening_price = post_data.get('opening_price')
    highest_price = post_data.get('highest_price')
    lowest_price = post_data.get('lowest_price')
    closing_price = post_data.get('closing_price')
    date_time = post_data.get('date_time')

    try:
        stocks = Stocks(
            stock_name=stock_name, opening_price=opening_price,
            highest_price= highest_price, lowest_price=lowest_price,
            closing_price=closing_price,
            date_time=date_time
        )
        db.session.add(stocks)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'New stocks was recorded!',
            'data': {
                "stock_name": stocks.stock_name,
                "opening_price": stocks.opening_price,
                "highest_price":  stocks.highest_price,
                "lowest_price": stocks.lowest_price,
                "closing_price": stocks.closing_price,
                "date_time": stocks.date_time,
            }
        }
        return jsonify(response_object), 201
    except (exc.IntegrityError, ValueError) as e:
        db.session().rollback()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload'
        }
        return jsonify(response_object), 400

@stocks_blueprint.route('/get/stocks/', methods=['GET'])
def get_stocks():
    stocks = Stocks.query.all()
    results = []
    for item in stocks:
        results.append({
            "stock_name": item.stock_name,
            "opening_price": item.opening_price,
            "highest_price":  item.highest_price,
            "lowest_price": item.lowest_price,
            "closing_price": item.closing_price,
            "date_time": item.date_time,
        })
    return jsonify({ 
      'status': 'success', 
      'data': results
    }), 200
