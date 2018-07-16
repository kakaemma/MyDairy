from flask import jsonify
from validate_email import validate_email

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
            response = jsonify({'Conflict': 'Invalid email address'})
            response.status_code = 400
            return response

        if len(password) < 5:
            response = jsonify({'Error': 'Password too short'})
            response.status_code = 422
            return response
