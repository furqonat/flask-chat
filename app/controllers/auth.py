from flask import Blueprint, redirect, request, url_for, session

from app.utils import view
from ..services import authenticate_account, create_new_account

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["GET", "POST"])  # type: ignore
@view("pages/auth/login.html")
def login():
    if request.method == "GET":
        is_authenticated = session.get("user_uid", None)
        if is_authenticated:
            return redirect(url_for("chat.index"))
        return {}
    else:
        return action_login()


def action_login():
    email = request.form.get("Email", None)
    password = request.form.get("password", None)
    print(email, password)
    account = authenticate_account(email, password)
    if account:
        session["user_uid"] = account.uid
        return redirect(url_for("chat.index"))
    else:
        return {"error": "Invalid credentials"}


@auth.route("/register", methods=["GET", "POST"])  # type: ignore
@view("pages/auth/register.html")
def register():
    if request.method == "GET":
        is_authenticated = session.get("user_uid", None)
        if is_authenticated:
            return redirect(url_for("chat.index"))
        return {}
    else:
        return action_register()


def action_register():
    name = request.form.get("Name", None)
    email = request.form.get("Email", None)
    password = request.form.get("Password", None)
    account = create_new_account(name, email, password)
    if account:
        return redirect(url_for("auth.login"))
    else:
        return {"error": "Account creation failed"}


@auth.route("/forgot-password", methods=["GET", "POST"])  # type: ignore
@view("pages/auth/forgot_password.html")
def forgot_password():
    if request.method == "GET":
        return {}
    else:
        action_forgot_password()


def action_forgot_password():
    # TODO: send email to reset password
    pass
