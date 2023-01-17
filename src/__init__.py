import time
import traceback
import os
import importlib

def create_app():
    from flask import Flask
    from src import blueprints
    from src.ext import auth
    
    app = Flask(__name__)
    app.secret_key = 'sdklj(gn452g%pçn*sdfjkg_vndsnf9i43rh&oiqecvn!njkfdewrgfewr567i578hjkgm@pryar'
    auth.init_app(app)
    blueprints.init_app(app)
    
    return app


class Server:
    def __init__(self, debug=True, port=8000, host='127.0.0.1'):
        self.debug = debug
        self.port = port
        self.host = host
    
    def run(self):
        while True:
            try:
                import src
                importlib.reload(src)
                self.app = create_app()
                self.app.run(debug=self.debug, host=self.host, port=self.port)
            except Exception:
                os.system('clear')
                print(traceback.format_exc())
                time.sleep(1)
