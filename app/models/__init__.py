from flask import Blueprint



bp = Blueprint('models',__name__,template_folder='template')
from .user import *
from .category import *
from .product import *
from .imgs import *
from .order import *
