from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id':fields.Integer(required=True, decription='user id'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'email': fields.String(required=True, description='user email'),
        'password': fields.String(required=True, description='user password'),
        #'dob_at': fields.Integer(required=True,description='user dob'),
        'gen': fields.String(required=True, description='gender'),
    })

    res_sources = api.model('response of all sources', {
        'items': fields.List(fields.Nested(user),attribute="items",)
    })

   


    

