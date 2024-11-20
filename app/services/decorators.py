from flask import session,redirect,url_for,flash




def super_session_required(user_types=[],permissions={},):
    def wrapper(f):
        def wrapped_function(*args, **kwargs):
            unauthorized = False
            if "superAdmin" in session and session.get("superAdmin") == True :
                return f(*args, **kwargs)
            else:
                flash("You Need To Login First")
            return redirect(url_for("superAdmin.login"))
        wrapped_function.__name__ = f.__name__
        return wrapped_function
    return wrapper