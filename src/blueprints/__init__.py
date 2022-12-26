from src.blueprints import users
from flask import Flask

def init_app(app: Flask):
    app.register_blueprint(users.bp)