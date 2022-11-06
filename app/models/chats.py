from dataclasses import dataclass
from datetime import datetime
from typing import Union

from app.utils import MAX_MESSAGE_LENGTH, db, generate_uuid


@dataclass
class Chats(db.Model):  # type: ignore

    uid: Union[str, db.Column] = db.Column(
        db.String(36), primary_key=True, default=generate_uuid
    )
    message: Union[str, db.Column] = db.Column(
        db.Text(MAX_MESSAGE_LENGTH), nullable=False
    )
    created_at: Union[datetime, db.Column] = db.Column(
        db.DateTime, nullable=False, default=datetime.now()
    )
    owner: Union[str, db.Column] = db.Column(
        db.String(36), db.ForeignKey("accounts.uid"), nullable=False
    )
    deleted: Union[bool, db.Column] = db.Column(
        db.Boolean, nullable=False, default=False
    )
