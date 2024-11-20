from .. import bp
from app.services.auth import auth
from flask import jsonify

@bp.route('/tokens',methods=['POST'])
@auth.login_required
def token():
    basic_auth = auth.current_user()
    token_details = basic_auth.get_token()
    return jsonify(token_details)