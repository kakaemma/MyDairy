import datetime


class DiaryModel(object):
    """ This class handles all model operations to the diary"""
    diary = []

    def __init__(self, first_name, last_name, email, password ):
        """
        This constructor initialises all the parameters
        :param first_name: 
        :param last_name: 
        :param email: 
        :param password: 
        """
        self.diary_id = len(DiaryModel.diary)+1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.date_created = datetime.datetime.utcnow()
        self.date_modified = None

    def create_diary(self):
        """
        Adds diary model object to diary list
        :return: 
        """
        DiaryModel.diary.append(self)
        return self.diary_id

