from dataclasses import dataclass
from typing import Union

from ..utils import db, generate_uuid
from .room import chat_room


@dataclass
class Accounts(db.Model):  # type: ignore

    uid: Union[str, db.Column] = db.Column(
        db.String(36), primary_key=True, default=generate_uuid
    )
    name: Union[str, db.Column] = db.Column(db.String(255), nullable=False)
    email: Union[str, db.Column] = db.Column(
        db.String(255), nullable=False, unique=True
    )
    password: Union[str, db.Column] = db.Column(db.String(255), nullable=False)
    chats: db.relationship = db.relationship(  # type: ignore
        "Chats", backref="Accounts", lazy=True, secondary=chat_room
    )
