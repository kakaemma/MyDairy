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
        self.date_created = datetime.datetime.utcnow()
        self.date_modified = None

    def create_user(self):
        """
        Adds user model object to user list
        :return: 
        """
        UserModel.user.append(self)
        return self.user_id

    @staticmethod
    def check_if_email_exists(email):
        for this_user in UserModel.user:
            if this_user.email == email:
                return this_user.email
