from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from ..utils import db, bcrypt

from ..models.accounts import Accounts


def create_new_account(
    name: Optional[str], email: Optional[str], passowrd: Optional[str]
) -> Optional[Accounts]:
    try:
        account = Accounts(
            name=name, email=email, password=bcrypt.generate_password_hash(passowrd)
        )
        db.session.add(account)
        db.session.commit()
        return account
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e


def get_account_by_email(email: str) -> Optional[Accounts]:
    return db.session.execute(
        db.select(Accounts).where(Accounts.email == email)
    ).scalar_one_or_none()


def get_account_by_uid(uid: str) -> Optional[Accounts]:
    return db.session.execute(
        db.select(Accounts).where(Accounts.uid == uid)
    ).scalar_one_or_none()


def delete_account_by_uid(uid: str) -> Optional[bool]:
    try:
        db.session.execute(db.delete(Accounts).where(Accounts.uid == uid))
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e
    return True


def authenticate_account(
    email: Optional[str], password: Optional[str]
) -> Optional[Accounts]:
    if email and password:
        account: Optional[Accounts] = get_account_by_email(email)
        if account and bcrypt.check_password_hash(account.password, password):
            return account
        return None
    else:
        raise AttributeError("email and password are required")
