from flask import request, jsonify
import os
from flask_jwt import jwt
from functools import wraps


"""decorator function to validate JWT"""


def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwds):

        token = request.headers.get('Authorization')
        if not token:
            return jsonify(error='unauthorized'), 401
        try:
            data = jwt.decode(token, os.environ['SECRET_KEY'])
        except:
            return jsonify(error='unauthorized'), 401
        return func(*args, **kwds)
    return wrapped
