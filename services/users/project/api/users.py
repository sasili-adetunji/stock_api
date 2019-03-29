import os
from flask import Flask, jsonify, Blueprint

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users/ping', methods=['GET']) 
def ping_pong():
    return jsonify({ 
      'status': 'success', 
      'message': 'pong!'
})