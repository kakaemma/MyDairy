from flask import jsonify,request,json,render_template
from classes.auth import Authentication
from classes.diary import Diary
from classes.item import DiaryItem
from utility.utility import validate_token, validate_content_type
from api import create_app


app = create_app('ProductionEnv')

@app.route('/')
def index():
    """
    Index route
    :return: 
    """
    return render_template('index.html')


@app.route('/api/<version>/register', methods=['POST'])
def register(version):
    """
    This end point registers a user
    :param version: 
    :return: 
    """
    request.get_json(force=True)
    try:
        first_name = request.json['f_name']
        last_name = request.json['l_name']
        email = request.json['email']
        password = request.json['password']
        response = Authentication.registration(first_name,
                                               last_name, email, password)
        return response

    except KeyError:
        invalid_keys()


@app.route('/api/<version>/login', methods=['POST'])
def login(version):
    try:
        request.get_json(force=True)
        email = request.json['email']
        password = request.json['password']
        login_user = Authentication.login(email, password)
        return login_user

    except KeyError:
        invalid_keys()


@app.route('/api/<version>/reset-password', methods=['POST'])
@validate_content_type
@validate_token
def reset_password(version):
    """
    End point for reset password
    """

    request.get_json(force=True)
    try:
        email = request.json['email']
        old_pass = request.json['password']
        new_pass = request.json['new_password']
        response = Authentication.reset_password(email, old_pass, new_pass)
        return response

    except KeyError:
        invalid_keys()


@app.route('/api/<version>/diary', methods=['POST'])
@validate_content_type
@validate_token
def add_diary(version):
    try:
        request.get_json(force=True)
        diary_name = request.json['name']
        response = Diary.new_diary(diary_name)
        return response

    except KeyError:
        invalid_keys()

@app.route('/api/<version>/diary', methods=['GET'])
@validate_token
def get_diaries(version):
    try:
        response = Diary.get_diaries()
        return response

    except KeyError:
        invalid_keys()

@app.route('/api/<version>/diary/<int:diary_id>', methods=['GET'])
@validate_token
def get_single_diary(version, diary_id):
    try:
        response = Diary.get_diary(diary_id)
        return response

    except KeyError:
        invalid_keys()

@app.route('/api/<version>/diary/<int:diary_id>', methods=['PUT'])
@validate_content_type
@validate_token
def modify_diary(version, diary_id):
    try:
        request.get_json(force=True)
        name = request.json['name']
        response = Diary.edit_diary(diary_id, name)
        return response

    except KeyError:
        invalid_keys()

@app.route('/api/<version>/diary/<int:diary_id>/item', methods=['POST'])
@validate_content_type
@validate_token
def diary_description(version, diary_id):
    try:
        request.get_json(force=True)
        description = request.json['desc']
        response = DiaryItem.add_diary_description(diary_id, description)
        return response

    except KeyError:
        invalid_keys()


@app.route('/api/<version>/diary/<int:diary_id>/\
item/<int:item_id>', methods=['PUT'])
@validate_content_type
@validate_token
def edit_description(version, diary_id, item_id):
    try:
        request.get_json(force=True)
        description = request.json['desc']
        response = DiaryItem.edit_diary_description(\
            diary_id, item_id, description)
        return response

    except KeyError:
        invalid_keys()


@app.route('/api/<version>/diary/<int:diary_id>/item', methods=['GET'])
@validate_token
def get_description_for_diary(version, diary_id):
    try:
        response = DiaryItem.get_diary_descriptions(diary_id)
        return response

    except KeyError:
        invalid_keys()




def invalid_keys():
    """
    Handles invalid keys
    :return: 
    """
    response = jsonify({'Error': 'Invalid keys'})
    response.status_code = 400
    return response
