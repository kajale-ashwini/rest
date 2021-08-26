from flask import request
from flask_restplus import Resource
from app.main.model.user import User
from app.main.util.dto import UserDto
from app.main.config import Config
import datetime
from app.main.service.user_service import delete_user, save_new_user,get_all_users,get_a_user,delete_user

api = UserDto.api
_user = UserDto.res_sources



#@api.route("api/test")
#class Registration(Resource):
#    def get(self):
#        return {"manfo": "tandn"}

@api.route('api/save')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user)
    def get(self):
        """List all registered users"""
        return get_all_users()


    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('api/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, id):
        """get a user given its identifier"""
        user = get_a_user(id)
        if not user:
            api.abort(404)
        else:
            return user 

    
    @api.doc('get a user')
    @api.marshal_with(_user)
    def delete(self, id):
        """get a user given its identifier"""
        user = delete_user(id)
        return user
            

    

    



