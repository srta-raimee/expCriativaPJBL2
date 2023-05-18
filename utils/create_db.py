from models import *
from flask import Flask

def create_db(app:Flask):
    with app.app_context():
        db.create_all()
        # criar seeds
        # from utils.seeds import generate_seeds
        # generate_seeds(db) 