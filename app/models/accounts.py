from dataclasses import dataclass
from typing import Union

from sqlalchemy import Column, String

from ..utils import BaseModel, generate_uuid


@dataclass
class Accounts(BaseModel):
    __tablename__ = "accounts"

    uid: Union[str, Column] = Column(String(36), primary_key=True, default=generate_uuid)
    name: Union[str, Column] = Column(String(255), nullable=False)
    email: Union[str, Column] = Column(String(255), nullable=False, unique=True)
    password: Union[str, Column] = Column(String(255), nullable=False)
