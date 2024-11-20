import hashlib
import os
from app import create_app
from flask import send_from_directory,abort,current_app
from app import UPLOAD_FOLDER

def get_hash(value):
    hash_value = hashlib.sha256(value.encode('utf-8')).hexdigest()
    return hash_value


# UPLOAD_FOLDER = os.path.join(current_app.root_path, 'superAdmin', 'images')
def images(location):
    print(location,'loaction')
    # image_list = os.listdir(UPLOAD_FOLDER)
    # if not os.path.exists(os.path.join(UPLOAD_FOLDER, location)):
    #     return abort(404, description="Image not found")
    # return send_from_directory(UPLOAD_FOLDER,location)
    # location_name = img.location_name  # This is 'app/superAdmin/images/Screenshot_20230107-154703_WhatsApp.jpg'
    directory, filename = os.path.split(location)
    print('at imagessss',directory,filename)
    if not os.path.exists(os.path.join(UPLOAD_FOLDER,directory)):
        return abort(404,description=f"Image not Found {directory}")
    return send_from_directory(directory,filename)