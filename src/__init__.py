from flask import Flask, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from src.models import User
from src import blueprints
from src.ext import (
    auth
)

def create_app():
    app = Flask(__name__)
    app.secret_key = 'sdklj(gn452g%pçn*sdfjkg_vndsnf9i43rh&oiqecvn!njkfdewrgfewr567i578hjkgm@pryar'
    auth.init_app(app)
    blueprints.init_app(app)
    
    return app