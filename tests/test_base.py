import unittest
from flask import json
from api.diary import app
from instance.config import application_config

class BaseClass(unittest.TestCase):
    def setUp(self):
        app.config.from_object(application_config['TestingEnv'])
        self.client = app.test_client()

        self.empty_reg = json.dumps({
            'f_name': '',
            'l_name': '',
            'email': '',
            'password': ''
        })