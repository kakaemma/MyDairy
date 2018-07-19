import datetime


class UserModel(object):
    """ This class handles all model operations to the User"""
    user = []

    def __init__(self, first_name, last_name, email, password):
        """
        This constructor initialises all the parameters
        :param first_name: 
        :param last_name: 
        :param email: 
        :param password: 
        """
        self.user_id = len(UserModel.user)+1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def create_user(self):
        """
        Adds user model object to user list
        :return: 
        """
        UserModel.user.append(self)
        return self.user_id

    @staticmethod
    def check_if_email_exists(email):
        """
        This method checks if an email already exists
        :param email: 
        :return: 
        """
        for this_user in UserModel.user:
            if this_user.email == email:
                return this_user.email

    @staticmethod
    def check_if_user_is_valid(email, password):
        """
         This method checks if the email and 
         password exist in the system
         
        :param email: 
        :param password: 
        :return: 
        """
        for this_user in UserModel.user:
            if this_user.email == email and\
                            this_user.password == password:
                return this_user.user_id

    @staticmethod
    def reset_user_pass(email, new_password):
        for user in UserModel.user:
            if user.email == email:
                user.password = new_password
                response = user.user_id
                return response

    @staticmethod
    def get_user_by_id(user_id):
        for user in UserModel.user:
            if user.user_id == user_id:
                return user.user_id

    @staticmethod
    def check_user_return_pass(email):
        for user in UserModel.user:
            if user.email == email:
                response = user.password
                return response
