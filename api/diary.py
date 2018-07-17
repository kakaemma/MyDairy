from flask import jsonify,request,json,render_template
from classes.auth import Authentication
from api import create_app


app = create_app('DevelopmentEnv')

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

def invalid_keys():
    """
    Handles invalid keys
    :return: 
    """
    response = jsonify({'Error': 'Invalid keys'})
    response.status_code = 400
    return response