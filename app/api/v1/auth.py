from flask import Blueprint

auth_api = Blueprint(
    'auth_api',
    __name__,
    url_prefix='/api/v1/auth'
)


@auth_api.post('/login')
def login():
    return ""
