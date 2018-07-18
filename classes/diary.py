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
        added_diary = new_diary.create_diary()
        if added_diary:
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

    @classmethod
    def get_diary(cls, diary_id):

        if not diary_id:
            response = jsonify({'Error': 'Missing diary id'})
            response.status_code = 400
            return response

        diary_is_not_empty = DiaryModel.check_for_diaries()
        if diary_is_not_empty:
            single_diary = DiaryModel.check_diary_by_id(diary_id)
            if not single_diary:
                response = jsonify({'Info': 'Diary does not exist'})
                response.status_code = 404
                print(single_diary)

                return response

            this_diary = DiaryModel.get_diary_by_id(diary_id)

            response = jsonify({
                'Info': 'Diary retrieved',
                'Dairy': this_diary
            })
            response.status_code = 200
            return response




        response = jsonify({'Info': 'No diary entries added'})
        response.status_code = 400
        return response



