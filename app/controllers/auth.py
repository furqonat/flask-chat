from flask import Blueprint

from app.utils import view

auth = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth'
)


@auth.get('/login')
@view('auth/login.htm')
def login():
    return {'title': 'Halo dunia'}
