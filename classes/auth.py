from flask import jsonify
from validate_email import validate_email
from utility.utility import encode_auth_token
from models.user_model import UserModel

class Authentication(object):
    """
    This class handles user registration.
    Login and Registration
    """

    @staticmethod
    def registration(first_name, last_name, email, password):
        """
        This method handles user registration
        
        :param first_name: 
        :param last_name: 
        :param email: 
        :param password: 
        :return: 
        """
        if not first_name or not last_name\
                or not email or not password:
            response = jsonify({'Error':'Missing values'})
            response.status_code = 400
            return response

        if not validate_email(email):
            response = jsonify({'Error': 'Invalid email address'})
            response.status_code = 400
            return response

        if len(password) < 5:
            response = jsonify({'Error': 'Password too short'})
            response.status_code = 422
            return response

        if email == UserModel.check_if_email_exists(email):
            response = jsonify({'Conflict': 'Email already exists'})
            response.status_code = 409
            return response

        new_user = UserModel(first_name, last_name, email, password)
        user_id = new_user.create_user()
        if user_id:
            response = jsonify({'Info': 'User successfully registered '})
            response.status_code = 201
            return response

    @staticmethod
    def login(email, password):
        if not email or not password:
            response = jsonify({'Error': ' Missing login value(s)'})
            response.status_code = 422
            return response

        id_for_user = UserModel.\
            check_if_user_is_valid(email, password)
        if not id_for_user:
            response = jsonify({'Error': 'Invalid login credentials'})
            response.status_code = 400
            return response

        response = jsonify({
            'info': email + 'Login successful',
            'token': encode_auth_token(id_for_user).decode()
        })
        response.status_code = 200
        return response

    @staticmethod
    def reset_password(email, old_pass, new_pass):
        """
        Handles reset password
        :param email: 
        :param old_pass: 
        :param new_pass: 
        :return: 
        """
        if not email or not new_pass or not old_pass:
            response = jsonify({'Error': 'Missing email or password'})
            response.status_code = 400
            return response

        check_for_user_by_email = UserModel.check_user_return_pass(email)

        if not check_for_user_by_email or not old_pass == \
                check_for_user_by_email:
            response = jsonify({
                'Error': 'Email and password do not exist'
            })
            response.status_code = 401
            return response

        if old_pass == new_pass:
            response = jsonify({
                'Error': 'Old password and new password are the same'
            })
            response.status_code = 400
            return response

        reset_password = UserModel.reset_user_pass(email, new_pass)
        if reset_password:
            response = jsonify({'info': 'Password successfully changed'})
            response.status_code = 200
            return response
