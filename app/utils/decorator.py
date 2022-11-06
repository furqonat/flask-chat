from functools import wraps

from flask import render_template, redirect, session, url_for
from flask.wrappers import Response

def view(file_name: str, **kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwarg):
            # permissions = kwargs.get('permissions', None)
            require_auth = kwargs.get("require_auth", False)
            user_uid = session.get("user_uid", None)
            ctx = func(*args, **kwarg)
            if require_auth == True:
                if user_uid == None:
                    return redirect(url_for("auth.login"))
                return render_template(file_name, **ctx)
            if ctx is None:
                ctx = {}
            elif isinstance(ctx, tuple):
                ctx = dict(zip(kwargs.get("keys", []), ctx))
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(file_name, **ctx)

        return wrapper

    return decorator
