from app import db
from datetime import datetime
from pytz import timezone

class BaseBodel(db.Model):
    __abstract__ = True
    created_on = db.Column(db.DateTime,default = datetime.now(timezone('UTC')))
    updated_on = db.Column(db.DateTime,default = datetime.now(timezone('UTC')))