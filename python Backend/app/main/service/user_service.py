import uuid
from datetime import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    users = User.query.filter_by(email=data['email']).first()
    if not users:
        new_user = User(
             id=uuid.uuid4(),
             first_name=data['first_name'],
             last_name=data['last_name'],
             email=data['email'],
             password=data['password'],
             #dob_at=data['dob_at'],
             gen=data['gen'],
             
        )
        db.session.add(new_user)
        db.session.commit()
        response_object = {
            'success': True,
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': False,
            'message': 'User already exists.',
        }
        return response_object, 409


def get_all_users():
    """
    return all users
    """
    return {'items': User.query.all()}, 200


def get_a_user(id):
    """
    return user using id
    """
    return User.query.filter_by(id=id).first(), 200


def delete_user(id):
    '''function to delete a user from our database using
           the id of the user as a parameter'''
    user =  User.query.filter_by(id=id).delete()
    # filter user by id and delete
    db.session.delete()    # commiting the new change to our database
    
     


#def update_user(_id, _first_name, _last_name, _email, _password):
#       '''function to update the details of a user using the id, first_name,last_name,
#        email and password as parameters'''
#        user_to_update = User.query.filter_by(id=_id).first()
#        user_to_update.first_name = _first_name
#        user_to_update.last_name = _last_name
#        user_to_update.email = _email
#        user_to_update.password = _password
#        db.session.add(user_to_update)
#        db.session.commit()


