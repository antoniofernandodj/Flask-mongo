from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required, current_user
from src.models import User
from src.models import user_collection

bp = Blueprint('user', __name__)


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        user = User.validate_credentials(
            username=request.form.get('username'),
            password=request.form.get('password')
        )
        
        if user:
            login_user(user)
            return redirect(url_for('user.home'))
        else:
            return 'credenciais invalidas'
        
    return render_template('login.html')


@bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = User(
            name=request.form.get('name'),
            username=request.form.get('username'),
            password=request.form.get('password')
        )
        user.save()
        return 'usuario salvo com sucesso!'
        return redirect(url_for('user.login'))
        
    return render_template('signup.html')


@bp.route('/home/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@bp.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('user.login'))