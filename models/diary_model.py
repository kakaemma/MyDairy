import datetime


class DiaryModel(object):
    diary = []

    def __init__(self, name):
        """
        This constructor initialises diary
        :param name: 
        """
        self.diary_id = len(DiaryModel.diary)+1
        self.name = name
        self.date_created = datetime.datetime.utcnow()
        self.date_modified = None

    def create_diary(self):
        """
        Adds diary object to list
        :return: 
        """
        DiaryModel.diary.append(self)
        return self.diary_id
