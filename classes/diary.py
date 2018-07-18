from flask import jsonify
from models.diary_model import DiaryModel


class Diary(object):
    """ This class handles all operations on the diary"""

    @classmethod
    def new_diary(cls, name):
        """
        This method adds a new diary
        :param name: 
        :return: 
        """
        if not name:
            response = jsonify({'Error': 'Missing diary name'})
            response.status_code = 400
            return response

        new_diary = DiaryModel(name)
        if new_diary:
            response = jsonify({
                'info': 'Diary successfully added',
                            })
            response.status_code = 201
            return response


    @staticmethod
    def get_diaries():
        """
        This is responsible for getting all the diary 
        entries available in the system
        :return: 
        """

        diaries_available = DiaryModel.check_for_diaries()
        if diaries_available:
            diaries = DiaryModel.get_diaries()
            response = jsonify({
                'My Diary entries': diaries
            })
            response.status_code = 200
            return response

        response = jsonify({'Info': 'No diary entries available'})
        response.status_code = 404
        return response

