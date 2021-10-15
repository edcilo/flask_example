from functools import wraps
from flask import abort


def auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Validate authentication, return abort
        print(args, kwargs)
        return f(*args, **kwargs)
    return decorated_function
