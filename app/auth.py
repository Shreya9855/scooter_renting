from flask_restful import Resource,reqparse
from flask import jsonify
import json
from app.database import db_session
from app.models import User
from sqlalchemy import exc


parser = reqparse.RequestParser()
# parser.add_argument('name', required=True, help="Name cannot be blank!")
parser.add_argument('name')
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('confirmPassword')

class Register(Resource):
    def post(self):
        args = parser.parse_args()
        try:
            name = args["name"]
            email = args["email"]
            password = args["password"]
            confirmPassword = args["confirmPassword"]
            if password != confirmPassword:
                return jsonify({
                "Message" : "Password and Confirm password doesnot match.Please try again."
            })
            user = User(name=name,email=email,password=password)
            db_session.add(user)
            db_session.commit()
        except exc.IntegrityError: 
            return jsonify({
                "Message" : "The email has already been used.Please try again with new email."
            })
        print(user)
        return jsonify({
            'message' : 'New user created'
        })

    def get(self):
        users = User.query.all()
        user_list = []
        for user in users:
            print(user)
            user_list.append(user.name)
            user_list.append(user.email)
        return jsonify({
            "data" : user_list
        })

class Login(Resource):
    def post(self):
        args = parser.parse_args()
        email = args["email"]
        password = args["password"]
        check_user = User.query.filter(User.email == email).first()
        print(check_user.id)
        return jsonify({
            "data" : "User logged in"
        })

        
