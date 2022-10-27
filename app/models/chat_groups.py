from dataclasses import dataclass
from typing import Union

from sqlalchemy import Column, String, ForeignKey

from app.utils import BaseModel, generate_uuid


@dataclass
class ChatGroups(BaseModel):
    __tablename__ = "chat_groups"

    uid: Union[str, Column] = Column(String(36), primary_key=True, default=generate_uuid)
    account_uid: Union[str, Column] = Column(String(36), ForeignKey("accounts.uid"), nullable=False)
    chats_uid: Union[str, Column] = Column(String(36), ForeignKey("chats.uid"), nullable=False)
