from flask import Blueprint


bp = Blueprint('api',__name__,template_folder='templates')

from .user import *
from .common import *
from .products import *
from .common.token import *