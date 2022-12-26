from flask_login import LoginManager
from src.models import User


def init_app(app):
    lm = LoginManager()
    lm.init_app(app)
    
    @lm.user_loader
    def load_user(id):
        user = User.find(id=id)
        return user
