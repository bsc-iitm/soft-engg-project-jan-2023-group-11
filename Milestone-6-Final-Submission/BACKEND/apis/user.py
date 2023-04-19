from flask_restful import Resource
from flask import make_response, jsonify, Blueprint

from Models.user import User


class UserResource(Resource) :

    def post(self, username, password, usertype) :

        if User.get_user_by_username(username):

            msg = {'message' : "user already exist"}

            return make_response(jsonify(msg), 409)

        try :

            user = User(username=username, password=password, usertype=usertype)
            print("api")
            user.add_user()
            
            msg = {
                    'message' : 'User added successfully',
                    'user_id' : user._id,
                }

            return make_response(jsonify(msg), 201)

        except :

            msg = {'message' : 'An error occured while adding user'}
            return make_response(jsonify(msg), 500)


class UserLoginResource(Resource) :

    def get(self, username, password) :

        user = User.get_user_by_username(username)

        if user :

            try :
                
                if user.password == password :
                    
                    msg = {
                        'message' : 'user logged in successfully',
                        'user_id' : user._id
                        }
                    
                    return make_response(jsonify(msg), 200)
                msg = {'meassge' : "Wrong crendentials"}

                return make_response(jsonify(msg), 401)

            except :

                msg = {'message' : 'An error occured while logging in'}
                
                return  make_response(jsonify(msg), 500)
        
        msg = {'message' : 'User does exist with username or email . Please Sign Up !'}
        return make_response(jsonify(msg), 404)