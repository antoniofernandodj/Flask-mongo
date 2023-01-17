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

@bp.route('/example/')
def example():
    import dominate
    from dominate.tags import h1, div, span, p, link, br
    """Ou faça 'from dominate.tags import *' caso ponha no topo da página"""
    
    doc = dominate.document(title="teste")
    
    with doc.head:
        link(rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css",
            integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65",
            crossorigin="anonymous")
        link(rel="preconnect", href="https://fonts.googleapis.com")
        link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin='true')
        link(href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap", rel="stylesheet")

    with doc:
        with div(cls='text-center container', style="font-family: 'Pacifico', cursive;"):
            with h1(cls="mt-5 mb-3", style='font-size: 55px;'):
                span('Hello world!', cls="text-danger mb-5")
            
            with p(cls='mb-3 mt-5', style='font-size: 25px;'):
                span('''Este é um exemplo da biblioteca Dominate, sobre como
                     ela pode ser usada para gerar páginas web usando python''')
                
            with p(style='font-size: 25px;'):
                span('''Para melhorar e facilitar o servimento do html eu usei
                     uma rota de um app flask pré-existente.''')
                br()
                span('''Usei também bootstrap e para reduzir a quantidade de
                     código usado para gerar estilos.''')
                
            with p(style='font-size: 25px;'):
                span('''Para exibir esta fonte chata eu usei google fonts''')
                
    return doc.render(indent='', xhtml=True).replace('\n', '')