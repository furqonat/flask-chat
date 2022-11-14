from typing import Any, Optional

from sqlalchemy.exc import SQLAlchemyError

from ..models import Accounts, Chats
from ..utils import db


def create_new_chat(chat: Chats, group: Any) -> Optional[str]:

    try:

        group.chats.append(chat)

        db.session.add(group)
        db.session.commit()

    except SQLAlchemyError as e:

        db.session.rollback()

        return None

    return group.uid


def get_chat_by_group_uid(uid: str) -> Optional[list[Chats]]:

    return db.session.execute(db.select(Chats).where(Chats.group_uid == uid)).scalars()


def delete_chat_by_uid(uid: str) -> bool:

    try:

        db.session.execute(db.delete(Chats).where(Chats.uid == uid))
        db.session.commit()

    except SQLAlchemyError as e:

        db.session.rollback()

        return False

    return True


# TODO: implementation this method to get all chats from a group
def get_all_avaliable_user() -> Optional[list[Accounts]]:
    return db.session.execute(db.select(Accounts)).scalars()


# def delete_chat_group_by_uid(uid: str) -> bool:

#     try:

#         db.session.execute(db.delete(ChatRoom).where(ChatRoom.uid == uid))
#         db.session.commit()

#     except SQLAlchemyError as e:

#         db.session.rollback()

#         return False

#     return True
