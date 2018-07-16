from flask import jsonify,request,json,render_template
from api import create_app


app = create_app('DevelopmentEnv')

@app.route('/')
def index():
    """
    Index route
    :return: 
    """
    return render_template('index.html')