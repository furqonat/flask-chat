from flask import Blueprint, jsonify, session
from flask_socketio import emit, join_room, send

from app.services.account_services import get_account_by_uid

from ..services import get_all_avaliable_user, set_status_account
from ..utils import socket, validate_user, view

chat = Blueprint("chat", __name__, url_prefix="/chat")


@chat.get("/")  # type: ignore
@view("pages/chat/index.html", require_auth=True)
def index():
    users = get_all_avaliable_user()
    return {"chat_list": users}


@socket.on("connect")
@validate_user
def connect():
    user_id = session.get("user_uid", None)
    set_status_account(user_id, True)


@socket.on("disconnect")
@validate_user
def disconnect():
    user_id = session.get("user_uid", None)
    set_status_account(user_id, False)


@socket.on("message")
@validate_user
def message(data):
    emit("message", data, broadcast=True)


@socket.on("join")
@validate_user
def join(data):
    join_room(data["roomId"])
    user = get_account_by_uid(data["roomId"])
    send(message={'user': user, 'chat': 'chat'}, broadcast=True, to=data["roomId"])


@socket.on("user_status")
def user_status(data):
    print(data)
    emit("user_status", data, broadcast=True)
