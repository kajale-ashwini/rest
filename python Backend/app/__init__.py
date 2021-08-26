from flask_restplus import Api
from flask import Blueprint

from app.main.controller.user_controller import api as reg_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='website backend',
    version='1.0',
    description='rest api in flask',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(reg_ns, path='/')









#This clss is mainly concerned with view after running project GUI is displayed this class
#is responsible for that we have to import controller class here for the GUI