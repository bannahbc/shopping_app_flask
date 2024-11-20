from app import db
from .common.common import BaseBodel
from .imgs import Img
from .category import Category

class Product(BaseBodel):
    hash = db.Column(db.String(300),primary_key=True)
    produt_name = db.Column(db.String(300))
    description = db.Column(db.String(300))
    category_hash = db.Column(db.String(300))
    rating = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    price = db.Column(db.Integer)
    mrp = db.Column(db.Integer)
    offer = db.Column(db.Integer)

    is_active = db.Column(db.String(100))
    image1 = db.Column(db.String(300))
    image2 = db.Column(db.String(300))
    image3 = db.Column(db.String(300))



    def to_dict(self,propagation=0,cate_propagation=1):
        data = {
            "hash":self.hash,
            "product_name":self.produt_name,
            "description":self.description,
            "rating":self.rating,
            "stock":self.stock,
            'price':self.price,
            'mrp':self.mrp,
            'offer':self.offer,
            'image1':self.image1,
            'image2':self.image2
        }
        if cate_propagation >0:
            cate_propagation -1
            if self.category_hash:
                category = Category.query.filter_by(hash=self.category_hash).first()
                if category:
                    data['category'] = category.name
        if propagation >0:
            # print('at proooooooooooooooo')
            propagation -=1
            if self.hash:
                # print('at imggggggggggggg')
                images = Img.query.filter_by(product_hash=self.hash).all()
                if images:
                    result = [item.to_dict() for item in images]
                    data['images'] = result
        return data