import os
from sqlalchemy import exc
from flask import Flask, jsonify, request, Blueprint
from project.api.models import Stocks
from project.api.utils import authenticate
from project import db
import datetime
from dateutil import parser


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
    date = post_data.get('date')

    try:
        stocks = Stocks(
            stock_name=stock_name, opening_price=opening_price,
            highest_price= highest_price, lowest_price=lowest_price,
            closing_price=closing_price,
            date=date
        )
        db.session.add(stocks)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'New stocks was recorded',
            'stocks': stocks.to_json()
        }
        return jsonify(response_object), 201
    except (exc.IntegrityError, ValueError) as e:
        db.session().rollback()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload'
        }
        return jsonify(response_object), 400

@stocks_blueprint.route('/stocks/', methods=['GET'])
def get_stocks():

    begin_date = request.args.get('begin_date')
    end_date = request.args.get('end_date')

    if (begin_date and end_date):
        try:
            parsed_begin = parser.parse(begin_date)
            parsed_end = parser.parse(end_date)

        except:
            return jsonify({
                    'status': 'fail',
                    'message': 'Invalid date'
                }), 400
        stocks = Stocks.query.filter(Stocks.date.between(parsed_begin, parsed_end)).all()
    else:
        stocks = Stocks.query.all()

    results = []
    for stock in stocks:
        results.append({
            'stocks': stock.to_json()
        })
    return jsonify({ 
      'status': 'success', 
      'data': results
    }), 200
