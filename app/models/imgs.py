from app.models.common.common import BaseBodel
from app import db
from app.services.operations import images

class Img(BaseBodel):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    order = db.Column(db.Integer)
    product_hash = db.Column(db.String(300))
    location_name = db.Column(db.String(300))
    name = db.Column(db.Text)
    type = db.Column(db.Text)

    def to_dict(self):
        data = {
            "id":self.id,
            "order":self.order,
            "product_hash":self.product_hash,
            "location_name":self.location_name,
            "name":self.name
        }
        print('at imagesssssssssss')
        if self.location_name:
            data['imageee'] = images(self.location_name)
        return data

