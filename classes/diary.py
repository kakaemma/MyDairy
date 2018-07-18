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

        check_name = DiaryModel.check_name(name)
        if check_name:
            response = jsonify({'Conflict': 'Diary name already exists'})
            response.status_code = 409
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
                return response

            this_diary = DiaryModel.get_diary_by_id(diary_id)

            response = jsonify({
                'Info': 'Diary retrieved',
                'Dairy': this_diary
            })
            response.status_code = 200
            return response

        response = jsonify({'Info': 'Attempting to retrieve on empty diary'})
        response.status_code = 400
        return response

    @classmethod
    def edit_diary(cls, diary_id, diary_name):

        if not diary_id:
            response = jsonify({'Error': 'Missing diary id'})
            response.status_code = 422
            return response

        if not diary_name:
            response = jsonify({'Error': 'Missing diary name'})
            response.status_code = 422
            return response

        diary_with_data = DiaryModel.check_for_diaries()
        if not diary_with_data:
            response = jsonify({'Error': 'Attempting to edit on empty diary'})
            response.status_code = 400
            return response

        diary_entry = DiaryModel.check_diary_by_id(diary_id)
        if not diary_entry:
            response = jsonify({'Error': 'Diary does not exist'})
            response.status_code = 400
            return response

        edit_entry = DiaryModel.edit_diary(diary_id, diary_name)
        if not edit_entry:
            response = jsonify({'Error': 'Can not edit diary with the same name'})
            response.status_code = 400
            return response

        response = jsonify({'Info': 'Diary successfully modified'})
        response.status_code = 200
        return response
