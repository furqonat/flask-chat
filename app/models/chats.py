from dataclasses import dataclass
from datetime import datetime
from typing import Union

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Boolean

from app.utils import BaseModel, generate_uuid, MAX_MESSAGE_LENGTH


@dataclass
class Chats(BaseModel):
    __tablename__ = "chats"

    uid: Union[str, Column] = Column(String(36), primary_key=True, default=generate_uuid)
    message: Union[str, Column] = Column(Text(MAX_MESSAGE_LENGTH), nullable=False)
    created_at: Union[datetime, Column] = Column(DateTime, nullable=False, default=datetime.now())
    owner: Union[str, Column] = Column(String(36), ForeignKey('Accounts.uid'), nullable=False)
    deleted: Union[bool, Column] = Column(Boolean, nullable=False, default=False)
