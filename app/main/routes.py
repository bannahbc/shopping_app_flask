from . import bp
from flask import redirect,url_for


@bp.route('/')
@bp.route('/index')
def main():
    return redirect(url_for('superAdmin.login'))