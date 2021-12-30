from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()

def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    

    api = Api(app)
    from .api import people
    from .api import place
    from .api import trace
    api.add_resource(people.Api_of_People, "/people")
    api.add_resource(place.Api_of_Place, "/place")
    api.add_resource(trace.Api_Of_Trace, "/trace")

    # db.create_all(app=app)

    return app