from . import bp
from flask import request,jsonify,send_from_directory,current_app
from app.models.product import Product
from app.models.imgs import Img
import os

@bp.route('/cc')
def cc():
     return jsonify('hello world')
@bp.route('/get/<hash>')
def get(hash):
     im = Img.query.filter_by(id=hash).first()
     print(im.location_name,'location name')
     iUrl = os.path.join(current_app.root_path+im.location_name)
     print(iUrl,'jjjjj')
    #  with open('H:\my projects\flask\shopping_flask\app\superAdmin\images\Screenshot_8.png','rb') as imagefile:
    #       im_data = imagefile.read()
    #       print('image',im_data)
    #  print('print',os.path.join(current_app.root_path,"superAdmin\images"))
    #  check =os.path.isdir(os.path.join(current_app.root_path ,"superAdmin\images"))
    #  image_url = os.path.join(current_app.root_path,im.location_name)
    #  print(current_app.root_path,'images urrrrrrrrrrrrrr')
    #  k = send_from_directory(os.path.join(current_app.root_path ,"superAdmin\images"),"\Screenshot_8.png")
    #  f,h = os.path.split(im.location_name)
    #  p = os.getcwd()
    #  s = os.path.join(os.path.join(p,current_app.root_path),f)
    #  print('s',s)
     
     return str(iUrl+'/'+im.name)
@bp.route('/product/<hash>')
def getProduct(hash):
    # try:
        product = Product.query.filter_by(hash=hash).first()
        if not product:
            return jsonify({'error':'product not found'}),400
        return jsonify(product.to_dict())
    # except Exception as e:
        # return jsonify({'error':str(e)}),400   

@bp.route('/getProducts',methods=['GET'])
def getProducts():
    try:
        data = request.get_json()
        print('get,message',data)
        page = data.get('page') or 1
        per_page = data.get('per_page') or 20
        products = Product.query.paginate(page=page,per_page=per_page)
        product_dict = [item.to_dict() for item in products]
        result = {
            "page":page,
            "products":product_dict,
            "per_page":per_page
        }
        return jsonify({"result":result})
    except Exception as e:
        print(e)
        return jsonify({'error':"Smothing went wrong",'details':str(e)})
    

# import os
# from flask import Flask, render_template, send_from_directory

# app = Flask(__name__)

# # Route to serve individual images
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory('uploads', filename)

# # Route to display all images in the folder
# @app.route('/gallery')
# def gallery():
#     image_list = os.listdir('uploads')  # List all files in the 'uploads' folder
#     image_list = [img for img in image_list if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]  # Filter for image files
#     return render_template('gallery.html', images=image_list)

# if __name__ == '__main__':
#     app.run(debug=True)

