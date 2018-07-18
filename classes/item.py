from flask import jsonify
from models.diary_model import DiaryModel


class DiaryItem(object):

    @classmethod
    def add_diary_description(cls, diary_id, description):

        if not diary_id:
            response = jsonify({'Error': 'Missing diary id'})
            response.status_code = 400
            return response

        if not description:
            response = jsonify({'Error': 'Missing description'})
            response.status_code = 400
            return response

        check_diaries = DiaryModel.check_for_diaries()
        if not check_diaries:
            response = jsonify({'Info': 'Can not add description on empty diary'})
            response.status_code = 400
            return response
