from app import db
from .common.common import BaseBodel


class Category(BaseBodel):
    hash = db.Column(db.String(300),primary_key=True)
    name = db.Column(db.String(300))