from . import bp
from flask import jsonify,current_app,send_from_directory
from app.models.product import Product
from app.models.imgs import Img
import os
from app import UPLOAD_FOLDER


@bp.route('/products')
def main():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@bp.route('/im/<hash>')
def im(hash):
    print(hash,'hash')
    # product = Product.query.filter_by(hash=hash).first()
    path =os.path.join( current_app.root_path , current_app.config['UPLOAD_FOLDER'])
    # print(UPLOAD_FOLDER,'ccc',current_app.config['UPLOAD_FOLDER'])
    # print(path,'current path',current_app.root_path)
    # path = path.replace(r'\app\app', r'\app')
    # print('print',path)
    # f,m = slice(product.image1)
    # image = Img.query.filter_by(id=hash).first()
    # print(image.location_name,'imgage')
    # im = current_app.root_path + image.location_name + image.name
    # print('img',im)
    return (send_from_directory(path,hash))


@bp.route('/image/<filename>')
def getImgage(filename):
    path = os.path.join(current_app.root_path,UPLOAD_FOLDER)
