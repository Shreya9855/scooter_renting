from flask import Flask
from app.auth import Login, Register
from app.database import db_session,init_db
from flask_restful import Resource,Api

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    init_db()
    api = Api(app)

    class Index(Resource):
        def get(self):
            return {"hello" : "world"}
    
    api.add_resource(Index,"/")
    api.add_resource(Register,"/register")
    api.add_resource(Login,"/login")
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app