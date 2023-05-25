from flask import Flask, render_template, flash
from controllers.render import render
from controllers.user_controller import user
from controllers.sensors_controller import sensors
from controllers.devices_controller import dispositivos
from models.db import db, instance 
from flask_login import LoginManager

from models.db import db, instance 

def create_app() -> Flask:
    app = Flask(__name__, template_folder="./views/", static_folder="./static/", root_path="./")

    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance

    db.init_app(app)

    app.register_blueprint(render, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'render.pag_log'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):


        return User.query.get(int(user_id))

    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(sensors, url_prefix='/sensors')
    app.register_blueprint(dispositivos, url_prefix='/dispositivos')


    @app.route('/')
    def index():
        return render_template("home.html")

    return app

