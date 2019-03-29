import os
from flask import Flask, jsonify, Blueprint

stocks_blueprint = Blueprint('stocks', __name__)

@stocks_blueprint.route('/stocks/ping', methods=['GET']) 
def stocks_pong():
    return jsonify({ 
      'status': 'success', 
      'message': 'stocks'
})