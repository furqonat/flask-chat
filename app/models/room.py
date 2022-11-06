from ..utils import db, generate_uuid

chat_room = db.Table(
    "chat_room",
    db.Column(
        "uid",
        db.String(36),
        primary_key=True,
        default=generate_uuid,
    ),
    db.Column("chat_uid", db.String(36), db.ForeignKey("chats.uid")),
    db.Column("account_uid", db.String(36), db.ForeignKey("accounts.uid")),
)
