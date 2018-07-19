from functools import wraps
import datetime
from models.user_model import UserModel
from flask import request, jsonify
import jwt


def get_token():

    try:
        token = request.headers.get('Authorization')
        return token
    except Exception as ex:
        return ex
def method_to_be_returned(function, *args, **kwargs):

    try:
        if len(args) == 0 and len(kwargs) == 0:
            return function()
        else:
            return function(*args, **kwargs)
    except Exception as exc:
        response = jsonify({'Failed with Exception': exc})
        response.status_code = 500
        return response

def validate_content_type(func):

    @wraps(func)
    def decorated_method(*args, **kwargs):
        if request.headers.get('content-type') != 'application/json':
            response = jsonify({
                'Error': 'Content-Type not specified as application/json'
            })
            response.status_code = 400
            return response
        return method_to_be_returned(func, *args, **kwargs)
    return decorated_method

def encode_auth_token(user_id):

    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub':user_id
        }
        auth_token = jwt.encode(
            payload,
            '2018secret',
            algorithm='HS256'
        )
        return auth_token

    except Exception as ex:
        return ex

def decode_auth_token(token):
    try:
        payload = jwt.decode(token, '2018secret')
        user = payload['sub']
        return user
    except jwt.ExpiredSignature:
        return 'Token expired please login again'

    except jwt.InvalidTokenError:
        return 'Invalid token. Please login again \n'

def validate_token(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = get_token()
        if token is None:
            response = jsonify(
                {
                    'Error': 'There is no token'
                })
            response.status_code = 401
            return response
        try:
            user_id = decode_auth_token(token)
            user = UserModel.get_user_by_id(user_id)
            if user is None:
                response = jsonify({
                    'Error': 'Mismatching or wrong token'
                })
                response.status_code = 401
                return response

        except Exception as ex:
            response = jsonify({
                'Failed with exception': ex
            })
            response.status_code = 500
            return response
        return method_to_be_returned(func, *args, **kwargs)
    return decorated_function



