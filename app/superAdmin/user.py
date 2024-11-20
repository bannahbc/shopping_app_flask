from . import bp
from flask import render_template,request,current_app,redirect,url_for,flash,session,jsonify,Response
from app.models.user import UserProfile
from app.errors.types import RequestException
from app.services.decorators import super_session_required
from app.models.category import Category
import os
from werkzeug.utils import secure_filename
from app.models.imgs import Img,db
from app import UPLOAD_FOLDER,allowed_file

from app.models.product import Product
from app.models.category import Category
from app.models.imgs import Img
from app.services.operations import get_hash
from datetime import datetime
import random



@bp.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print("user",email)
        user = UserProfile.query.filter_by(email=(email.strip().lower())).first()
        if not user:
            flash('User Not Found')
            return redirect(url_for('superAdmin.login'))
        if not user.password_hash == password:
            flash('Password is Wrong')
            return redirect(url_for('superAdmin.login'))
        if not user.role == "superAdmin":
            flash('User Can Not Login')
            return redirect(url_for('superAdmin.login'))
        session['superAdmin'] = True
        session.permanent = True
        return redirect(url_for('superAdmin.home'))

    return render_template('login.html')

@bp.route('/createCategory',methods=['POST'])
def createCategory():
    try:
        data = request.get_json()
        catName = data.get('categoryName')
        cate_query = Category.query
        chech_cate = cate_query.filter_by(name=catName).first()
        
        if chech_cate:
            return jsonify({'message': 'Category Already Exists'}), 400
        hash = get_hash(str(random.random()+random.random()))
        cate_add = Category(hash=hash,name=catName)
        db.session.add(cate_add)
        db.session.commit()
        return jsonify({'message': 'Category Added Successfully!'}), 201
    except Exception as e:
        print('errorrrrr',e)
        db.session.rollback()  # Rollback in case of an error
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

@bp.route('/home',methods=['POST','GET'])
# @super_session_required()
def home():
    if request.method == 'POST':
        try:
            print('Post')
            description = request.form.get('description')
            name = request.form.get('productName')
            product = Product.query.filter_by(produt_name=name).first()
            if product:
                return jsonify({'error':'Product Already Exist!'}),400
            category_hash = request.form.get('category_select')
            product_hash = get_hash(str(datetime.now()))
            mrp = request.form.get('mrp')
            price = request.form.get('price')
            offer = request.form.get('offer')
            stock = request.form.get('stock')
            # imgs = request.files['imgs']
            imgs = request.files.getlist('imgs')
    
            image_d ={
                "image1":"",
                "image2":"",
                "image3":""
            }
            location_name = os.path.join( current_app.root_path,current_app.config['UPLOAD_FOLDER'])
            if imgs:
                for index,img in enumerate(imgs[:3]):
                    filename = secure_filename(img.filename)
                    if filename:
                        print('at i save',os.path.exists(location_name),os.path.exists(location_name))
                        if not os.path.exists(location_name):
                            os.makedirs(location_name)
                        im = "image"+str(index+1)
                        image_d[im]=filename
                        print(filename,'filneameeeeee',os.path.join(location_name,filename))

                        img.save(os.path.join(location_name,filename))
                        # image = Img(order=index+1,product_hash = product_hash,name=img.filename,location_name = location_name)
                        # db.session.add(image)
            

            # filename = secure_filename(imgs.filename)
            img_location = None

        # Check if the directory exists, if not, create it
            # if not os.path.exists(upload_folder):
            #     os.makedirs(upload_folder)
            # # print('dir',upload_folder)
            # if allowed_file(filename) and  not imgs=='':
            # # Save the file to the UPLOAD_FOLDER
            #     imgs.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            #     img_location = UPLOAD_FOLDER +imgs.filename

                # product = Product(image1=filename,image2=UPLOAD_FOLDER)
            product = Product(image1=image_d["image1"],image2=image_d["image2"],image3=image_d["image3"],hash=product_hash,produt_name = name,category_hash=category_hash,description=description,stock=stock,mrp=mrp,price=price,offer=offer)
            db.session.add(product)
            db.session.commit()
            # mimtype = imgs.mimetype
            # pic = Img(img=imgs.read(),minn=imgs.mimetype,name=filename)
            # print(pic,"pic",filename,"filename")
            # db.session.add(pic)
            # db.session.commit()
            return jsonify({'message':'PRODUCT ADDED SUCCESSFULLY'})
            # flash('PRODUCT ADDED SUCCESSFULLY ')
        except Exception as e:
            print(e,'pppppppppppp')
            return jsonify({'error': 'An error occurred', 'details': str(e)}), 500
            # flash('ERROR OCCURED WHILE ADDING NEW PRODUCT ')
        

    categories = Category.query.all()
    return render_template('home.html',categories=categories)

@bp.route('/ims/<int:id>')
def ims(id):
    img = Img.query.filter_by(hash=id).first()
    return Response(img.name,mimetype=img.minn)


# file save

# from werkzeug.utils import secure_filename
# import os
# from flask import current_app

# imgs = request.files.getlist('imgs')
# if imgs:
#     for index, img in enumerate(imgs[:3]):
#         filename = secure_filename(img.filename)
#         file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
#         img.save(file_path)
        
#         image = Img(order=index + 1, product_hash=product_hash, name=filename, location_name=file_path)
#         db.session.add(image)
    
#     db.session.commit()



# <!-- Category Form -->
# <form id="categoryForm" action="{{ url_for('superAdmin.create') }}" method="post">
#     <input type="hidden" name="form_type" value="category">
#     <input type="text" name="categoryName" placeholder="Category Name">
#     <button type="submit">Add Category</button>
# </form>

# <!-- Product Form -->
# <form id="productForm" action="{{ url_for('superAdmin.create') }}" method="post">
#     <input type="hidden" name="form_type" value="product">
#     <input type="text" name="productName" placeholder="Product Name">
#     <input type="number" name="productPrice" placeholder="Product Price">
#     <button type="submit">Add Product</button>
# </form>

# two or more forms
# @bp.route('/create', methods=['POST'])
# def create():
#     form_type = request.form.get('form_type')

#     if form_type == 'category':
#         # Handle category creation
#         cat_name = request.form.get('categoryName')
#         existing_category = Category.query.filter_by(name=cat_name).first()
        
#         if existing_category:
#             return jsonify({'message': 'Category already exists'}), 400
        
#         new_category = Category(name=cat_name)
#         db.session.add(new_category)
#         db.session.commit()
        
#         return jsonify({'message': 'Category added successfully!'}), 201

#     elif form_type == 'product':
#         # Handle product creation
#         product_name = request.form.get('productName')
#         product_price = request.form.get('productPrice')
        
#         new_product = Product(name=product_name, price=product_price)
#         db.session.add(new_product)
#         db.session.commit()
        
#         return jsonify({'message': 'Product added successfully!'}), 201

#     else:
#         return jsonify({'error': 'Invalid form submission'}), 400




# from flask import request, jsonify, flash
# import os
# from werkzeug.utils import secure_filename
# from datetime import datetime

# @bp.route('/addProduct', methods=['POST'])
# def add_product():
#     if request.method == 'POST':
#         try:
#             description = request.form.get('description')
#             name = request.form.get('productName')
#             category_hash = request.form.get('category_select')
#             product_hash = get_hash(str(datetime.now()))
#             mrp = request.form.get('mrp')
#             price = request.form.get('price')
#             offer = request.form.get('offer')
#             stock = request.form.get('stock')
#             imgs = request.files.getlist('imgs')
#             location_name = current_app.config['UPLOAD_FOLDER']

#             # Handle image upload
#             if imgs:
#                 for index, img in enumerate(imgs[:3]):
#                     filename = secure_filename(img.filename)
#                     if filename:
#                         img_location = os.path.join(location_name, filename)
#                         img.save(img_location)
#                         image = Img(order=index+1, product_hash=product_hash, name=filename, location_name=img_location)
#                         db.session.add(image)

#             # Add product to database
#             product = Product(
#                 hash=product_hash,
#                 produt_name=name,
#                 category_hash=category_hash,
#                 description=description,
#                 stock=stock,
#                 mrp=mrp,
#                 price=price,
#                 offer=offer
#             )
#             db.session.add(product)
#             db.session.commit()

#             # Return success message as JSON
#             return jsonify({'message': 'Product added successfully!'}), 201

#         except Exception as e:
#             db.session.rollback()  # Rollback if there's an error
#             return jsonify({'message': 'Error occurred while adding new product', 'error': str(e)}), 500

# <form id="productForm" action="{{ url_for('superAdmin.add_product') }}" method="post" enctype="multipart/form-data">
#     <input type="text" name="productName" placeholder="Product Name">
#     <textarea name="description" placeholder="Description"></textarea>
#     <input type="number" name="mrp" placeholder="MRP">
#     <input type="number" name="price" placeholder="Price">
#     <input type="number" name="offer" placeholder="Offer">
#     <input type="number" name="stock" placeholder="Stock">
#     <input type="file" name="imgs" multiple>
#     <button type="submit">Add Product</button>
# </form>

# <div id="message"></div>

# <script>
#     document.getElementById('productForm').addEventListener('submit', async function(e) {
#         e.preventDefault(); // Prevent the default form submission

#         const formData = new FormData(this); // Create FormData from form

#         try {
#             const response = await fetch(this.action, {
#                 method: 'POST',
#                 body: formData
#             });

#             const result = await response.json();
#             const messageDiv = document.getElementById('message');

#             if (response.ok) {
#                 messageDiv.textContent = result.message; // Show success message
#                 messageDiv.style.color = 'green';
#             } else {
#                 messageDiv.textContent = result.message || 'An error occurred';
#                 messageDiv.style.color = 'red';
#             }
#         } catch (error) {
#             console.error('Error:', error);
#             document.getElementById('message').textContent = 'An unexpected error occurred.';
#         }
#     });
# </script>
