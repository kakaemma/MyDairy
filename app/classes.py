from flask import jsonify
from validate_email import validate_email

from app.models import UserModel, DiaryModel, ItemModel
from app.utility import encode_auth_token


class Authentication(object):
    """
    This class handles user registration.
    Login and Registration
    """

    @staticmethod
    def registration(first_name, last_name, email, password):
        """
        This method handles user registration

        :param first_name: 
        :param last_name: 
        :param email: 
        :param password: 
        :return: 
        """
        if not first_name or not last_name \
                or not email or not password:
            response = jsonify({'Error': 'Missing values'})
            response.status_code = 400
            return response

        if not validate_email(email):
            response = jsonify({'Error': 'Invalid email address'})
            response.status_code = 400
            return response

        if len(password) < 5:
            response = jsonify({'Error': 'Password too short'})
            response.status_code = 422
            return response

        if email == UserModel.check_if_email_exists(email):
            response = jsonify({'Conflict': 'Email already exists'})
            response.status_code = 409
            return response

        new_user = UserModel(first_name, last_name, email, password)
        user_id = new_user.create_user()
        if user_id:
            response = jsonify({'Info': 'User successfully registered '})
            response.status_code = 201
            return response

    @staticmethod
    def login(email, password):
        if not email or not password:
            response = jsonify({'Error': ' Missing login value(s)'})
            response.status_code = 422
            return response

        id_for_user = UserModel. \
            check_if_user_is_valid(email, password)
        if not id_for_user:
            response = jsonify({'Error': 'Invalid login credentials'})
            response.status_code = 400
            return response

        response = jsonify({
            'info': email + 'Login successful',
            'token': encode_auth_token(id_for_user).decode()
        })
        response.status_code = 200
        return response

    @staticmethod
    def reset_password(email, old_pass, new_pass):
        """
        Handles reset password
        :param email: 
        :param old_pass: 
        :param new_pass: 
        :return: 
        """
        if not email or not new_pass or not old_pass:
            response = jsonify({'Error': 'Missing email or password'})
            response.status_code = 400
            return response

        check_for_user_by_email = UserModel.check_user_return_pass(email)

        if not check_for_user_by_email or not old_pass == \
                check_for_user_by_email:
            response = jsonify({
                'Error': 'Email and password do not exist'
            })
            response.status_code = 401
            return response

        if old_pass == new_pass:
            response = jsonify({
                'Error': 'Old password and new password are the same'
            })
            response.status_code = 400
            return response

        reset_password = UserModel.reset_user_pass(email, new_pass)
        if reset_password:
            response = jsonify({'info': 'Password successfully changed'})
            response.status_code = 200
            return response


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
            response.status_code = 400
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
            response = jsonify({'Error': 'No diary matches the supplied id'})
            response.status_code = 400
            return response

        edit_entry = DiaryModel.edit_diary(diary_id, diary_name)
        if not edit_entry:
            response = jsonify({'Error': 'Can not edit diary with the same name'})
            response.status_code = 409
            return response

        response = jsonify({'Info': 'Diary successfully modified'})
        response.status_code = 200
        return response


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
            response = jsonify({'Error': 'Missing description'})
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
                 on non existing diary entry'})
            response.status_code = 400
            return response

        check_description = ItemModel.check_for_items()
        if not check_description:
            response = jsonify({'Info': 'No descriptions added'})
            response.status_code = 400
            return response

        check_item = ItemModel.check_item(item_id)
        if not check_item:
            response = jsonify({'Info': 'Description with \
            that id does not exist'})
            response.status_code = 404
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
                {'Error': 'Attempting to retrieve non existing entry'})
            response.status_code = 404
            return response

        diary_desc = ItemModel.get_descriptions(diary_id)
        response = jsonify({
            'Diary with id': diary_id,
            'Descriptions':diary_desc
        })
        response.status_code = 200
        return response
