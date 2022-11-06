from flask import Flask, json
from flask_wtf.csrf import CSRFProtect
from flask_minify import Minify

from app.controllers import auth, chat
from app.utils import bcrypt, db

app = Flask(
    __name__, static_folder="dist", static_url_path="/dist", template_folder="templates"
)


def application_factory():
    app.config.from_file("flask.config.json", load=json.load)
    csrf = CSRFProtect()
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    bcrypt.init_app(app)
    app.register_blueprint(auth)
    app.register_blueprint(chat)
    Minify(app=app, html=True, js=True, cssless=True)

    return app


if __name__ == "__main__":
    app_context = application_factory()
    app_context.app_context().push()
    app_context.run(debug=True)
