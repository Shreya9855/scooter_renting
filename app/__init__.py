from flask import Flask
from app.database import db_session,init_db

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    init_db()

    @app.route('/')
    def hello_world():
        return {'Hello' :  'World!'}

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app