from flask import jsonify


class Diary(object):
    """ This class handles all operations on the diary"""

    @staticmethod
    def new_diary(name):
        if not name:
            response = jsonify({'Error': 'Missing diary name'})
            response.status_code = 400
            return response
