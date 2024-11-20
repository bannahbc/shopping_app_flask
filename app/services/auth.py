from flask_httpauth import HTTPBasicAuth
from app.models.user import UserProfile
from app.errors.types import RequestException
from werkzeug.security import generate_password_hash,check_password_hash
import hashlib
auth = HTTPBasicAuth()


def hash(value):
    hashed_value = hashlib.sha256(value.encode('utf-8'))
    return hashed_value.hexdigest()



@auth.verify_password
def verify_password(email,password):
    print('email',email,password,'basic auth')
    p = generate_password_hash(password)
    user  = UserProfile.query.filter_by(email=email).first()
    if not user:
        raise RequestException(status_code=404,message="User Not Found!")
    if user.password_hash==password:
        return user
    else:
        raise RequestException(status_code=400,message="Password Wrong")