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

    @staticmethod
    def check_for_diaries():
        """ This checks whether there are any diary entries"""
        if len(DiaryModel.diary) >=1:
            return len(DiaryModel.diary)

    @staticmethod
    def get_diaries(self):
        all_diaries = []
        for this_diary in DiaryModel.diary:
            all_diaries.append({
                'id': this_diary.diary_id,
                'name': this_diary.name,
                'Date created': this_diary.date_created,
                'Date Modified': this_diary.date_modified

            })
        return all_diaries
