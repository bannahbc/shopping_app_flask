
from app import db
from .common.common import BaseBodel
from datetime import datetime,timedelta
import base64,os
from pytz import timezone
class UserProfile(BaseBodel):
    hash = db.Column(db.String(300),primary_key=True)
    name = db.Column(db.String(300))
    password_expiry = db.Column(db.String(300))
    password_hash = db.Column(db.String(300))
    is_active = db.Column(db.String(20))
    role = db.Column(db.String(100))
    email = db.Column(db.String(300),unique=True)
    address = db.Column(db.String(300))
    token = db.Column(db.String(300))
    token_expiry = db.Column(db.String(300))
    phone = db.Column(db.Integer)




    def get_token(self,expire_in = 60 * 60 * 1):
        now_asia = datetime.now(timezone('Asia/Kolkata'))
        now_asia = now_asia.replace(tzinfo=None)
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiry = now_asia + timedelta(seconds=expire_in)
        db.session.add(self)
        db.session.commit()
        return {
            "token":self.token,
            "expires_at":self.token_expiry
        }
