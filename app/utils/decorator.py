from functools import wraps
from flask import render_template, redirect, url_for
from htmlmin.minify import html_minify


def view(file_name: str, **kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwarg):
            # permissions = kwargs.get('permissions', None)
            if kwargs.get('required_auth', False):
                return redirect(url_for('auth.login'))
            # elif permissions and not any([permission in permissions for permission in kwargs.get('permissions', [])]):
            #     return redirect(url_for('auth.login'))
            return html_minify(render_template(file_name, **func(*args, **kwarg)))

        return wrapper

    return decorator

