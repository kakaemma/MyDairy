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

    @staticmethod
    def edit_diary_description(diary_id, item_id, desc):
        if not diary_id or not item_id:
            response = jsonify({'Error': 'Missing id for resource(s)'})
            response.status_code = 400
            return response

        if not desc:
            response = jsonify({'Error': 'Missing \
            description for diary item'})
            response.status_code = 400
            return response

        if len(desc) < 10:
            response = jsonify({'Error': 'Description must have\
             a minimum of 10 characters'})
            response.status_code = 400
            return response

        check_diaries = DiaryModel.check_for_diaries()
        if not check_diaries:
            response = jsonify({'Info': 'Can not edit \
            description on empty diary'})
            response.status_code = 400
            return response

        check_entry_exists = DiaryModel.check_diary_by_id(diary_id)
        if not check_entry_exists:
            response = jsonify(
                {'Error': 'Attempting to modify description\
                 on non existing entry'})
            response.status_code = 400
            return response

        edit_item = ItemModel.modify_description(diary_id, item_id, desc)
        if not edit_item:
            response = jsonify(
                {
                    'Error': 'Can not edit item with same description'
                })
            response.status_code = 400
            return response

        response = jsonify({'info': 'Description changed'})
        response.status_code = 200
        return response

    @classmethod
    def get_diary_descriptions(cls, diary_id):
        if not diary_id:
            response = jsonify({'Error': 'Diary id missing'})
            response.status_code = 400
            return response

        diaries = DiaryModel.check_for_diaries()
        if not diaries:
            response = jsonify({'Info': 'Can not retrieve \
            description on empty diary'})
            response.status_code = 400
            return response

        items = ItemModel.check_for_items()
        if not items:
            response = jsonify({'Info': 'No descriptions added'})
            response.status_code = 400
            return response

        entry_exists = DiaryModel.check_diary_by_id(diary_id)
        if not entry_exists:
            response = jsonify(
                {'Error': 'Attempting to retrieve\
                 on non existing entry'})
            response.status_code = 400
            return response

        diary_desc = ItemModel.get_descriptions(diary_id)
        response = jsonify({
            'Diary with id': diary_id,
            'Descriptions':diary_desc
        })
        response.status_code = 200
        return response





