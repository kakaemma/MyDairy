from flask import jsonify
from models.diary_model import DiaryModel
from models.item_model import ItemModel


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

        if len(description) < 10:
            response = jsonify({'Error': 'Description must have\
             a minimum of 10 characters'})
            response.status_code = 400
            return response

        check_diaries = DiaryModel.check_for_diaries()
        if not check_diaries:
            response = jsonify({'Info': 'Can not add description on empty diary'})
            response.status_code = 400
            return response

        check_entry_exists = DiaryModel.check_diary_by_id(diary_id)
        if not check_entry_exists:
            response = jsonify(
                {'Error': 'Attempting to add description\
                 on non existing entry'})
            response.status_code = 400
            return response

        add_description = ItemModel(diary_id, description)
        is_description_added = add_description.create_description()
        if is_description_added:
            response =jsonify({'info': 'Diary description added'})
            response.status_code = 201
            return response



