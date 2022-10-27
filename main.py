from flask import Flask

from app.controllers import auth

app = Flask(
    __name__,
    static_folder='dist',
    template_folder='templates'
)

app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)
