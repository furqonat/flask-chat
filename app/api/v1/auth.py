from flask import Blueprint, flash, make_response

auth_api = Blueprint(
    'auth_api',
    __name__,
    url_prefix='/api/v1/auth'
)


@auth_api.post('/login')
def login():
    response = make_response()
    response.set_cookie('')
    return ""
