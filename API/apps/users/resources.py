from flask import request

from flask_restful import Resource
from bcrypt import gensalt, hashpw
from marshmallow import ValidationError

from .models import User
from .schemas import UserSchema, UserRegistrationSchema