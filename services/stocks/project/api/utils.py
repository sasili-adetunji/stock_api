from functools import wraps

from flask import request, jsonify, current_app
import json
import requests


def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response_object = {
            'status': 'error',
            'message': 'Something went wrong'
        }
        code = 401
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            response_object['message'] = 'Kindly provide a valid auth token.'
            code = 403
            return jsonify(response_object), code
        auth_token = auth_header.split(" ")[1]
        response = ensure_authenticated(auth_token)
        if not response:
            response_object['message'] = 'The token is invalid.'
            return jsonify(response_object), code
        return f(response, *args, **kwargs)
    return decorated_function


def ensure_authenticated(token):
    if current_app.config['TESTING']:
        test_response = {
            'data': {'id': 12},
            'status': 'success',
        }
        return test_response
    url = '{0}/admin/status'.format(current_app.config['USERS_SERVICE_URL'])
    bearer = 'Bearer {0}'.format(token)
    headers = {'Authorization': bearer}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    if response.status_code == 200 and data['status'] == 'success':
        return data
    else:
        return False