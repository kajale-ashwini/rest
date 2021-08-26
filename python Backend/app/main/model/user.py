from enum import unique
from app.main import db
import calendar
import time
import uuid
from sqlalchemy.dialects.postgresql import UUID



class User(db.Model):
    __tablename__ = "sinew"
    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(100))
    #dob_at = db.Column(db.BIGINT, nullable=False, default=calendar.timegm(time.gmtime()))
    gen = db.Column(db.String(20), nullable=False)
    #gender = db.Column(db.ENUM('female', 'male'))
   

    def __init__(self, id, first_name, last_name,email,password,gen):
        self.id = id,
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        #self.dob_at = dob_at
        self.gen = gen
