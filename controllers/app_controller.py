from flask import Flask, render_template
from controllers.render import render
from controllers.user import user
from controllers.sensors import sensors
# from controllers.devices import devices

from models.db import db, instance 

def create_app() -> Flask:
    app = Flask(__name__, template_folder="./views/", static_folder="./static/", root_path="./")
    
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    
    db.init_app(app)

    app.register_blueprint(render, url_prefix='/')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(sensors, url_prefix='/sensors')
    # app.register_blueprint(devices, url_prefix='/devices')


    @app.route('/')
    def index():
        return render_template("home.html")
    
    return app
