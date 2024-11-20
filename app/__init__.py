from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
UPLOAD_FOLDER = 'static\images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''



def create_app(config_class = Config):
    app = Flask(__name__,static_folder='static')
    # @app.after_request
    # def after_request(response):
    #     response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    #     # response.headers.add('Access-Control-Allow-Origin', '*') for all request
    #     return response 
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app,db)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    CORS(app,resources={r"/api/*":{'origins':"*"}})

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api  import bp as api_bp
    app.register_blueprint(api_bp,url_prefix='/api')

    from app.models import bp as model_bp
    app.register_blueprint(model_bp)

    # from app.errors import bp as error_bp
    # app.register_blueprint(error_bp)

    from app.superAdmin import bp as superAdmin_bp
    app.register_blueprint(superAdmin_bp,url_prefix='/admin')

    return app