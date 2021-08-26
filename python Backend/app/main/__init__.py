from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.main.config import config_by_name

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    return app






#We’ve created a function, create_app that, given a configuration name, 
# loads the correct configuration from the app.main.config.py file
#We have also created a db object which we will use to interact with the database

#This will allow us to use SQLAlchemy, a useful tool for SQL use with Python. 
# SQLAlchemy is an Object Relational Mapper (ORM),
# which means that it connects the objects of an application to tables in a relational database management system.