import os
from flask import Flask, jsonify, Blueprint
from project.api.models import Stocks
from project.api.utils import authenticate

stocks_blueprint = Blueprint('stocks', __name__)

@stocks_blueprint.route('/stocks/ping', methods=['GET']) 
def stocks_pong():
    return jsonify({ 
      'status': 'success', 
      'message': 'stocks'
})

@stocks_blueprint.route('/stocks/', methods=['GET'])
@authenticate
def post_stocks(resp):
    if not resp['data']:
        response_object = {
            'status': 'error',
            'message': 'You do not have permission to do that.'
        }
        return jsonify(response_object), 401
    stocks = Stocks.query.all()
    return jsonify({
      'status': 'success',
      'stocks': stocks
    })