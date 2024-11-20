
from flask import Blueprint

bp = Blueprint('superAdmin',__name__,template_folder='templates',static_folder='static')

from .user import *