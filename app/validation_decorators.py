from functools import wraps
from flask import request, jsonify


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
