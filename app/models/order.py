from .common.common import BaseBodel
from app import db



class Order(BaseBodel):
    id = db.Column(db.Integer,primary_key = True)
    status = db.Column(db.String(100))
    count = db.Column(db.Integer)
    product_hash = db.Column(db.String(300))
    user_hash = db.Column(db.String(300))


    def to_dict(self):
        data = {
            "id":self.id,
            "status":self.status,
            "count":self.count,
            "product_hash":self.product_hash,
            "user_hash":self.user_hash
        }
        return data
