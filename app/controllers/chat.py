from flask import Blueprint

from ..utils import view

chat = Blueprint("chat", __name__, url_prefix="/chat")


@chat.get("/")  # type: ignore
@view("pages/chat/index.html", require_auth=True)
def index():
    return {}
