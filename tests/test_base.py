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
        self.invalid_email = json.dumps({
            'f_name': 'Emmanuel',
            'l_name': 'Kakaire',
            'email': 'kakaemma',
            'password': '123456'
        })
        self.short_password = json.dumps({
            'f_name': 'Emmanuel',
            'l_name': 'Kakaire',
            'email': 'kakaemma@gmail.com',
            'password': '1234'
        })
        self.user = json.dumps({
            'f_name': 'Emmanuel',
            'l_name': 'Kakaire',
            'email': 'kakaemma@gmail.com',
            'password': '1234567'
        })
        self.user_two = json.dumps({
            'f_name': 'Emmanuel',
            'l_name': 'Kakaire',
            'email': 'ekaka@gmail.com',
            'password': '1234567'
        })
        self.new_user = json.dumps({
            'f_name': 'Emmanuel',
            'l_name': 'Kakaire',
            'email': 'kakaemma1@gmail.com',
            'password': '1234567'
        })
        self.empty_login = json.dumps({
            'email':'',
            'password':''
        })
        self.invalid_user = json.dumps({
            'email':'kaka@gmail.com',
            'password':'xxddcc1'
        })
        self.invalid_login_email = json.dumps({
            'email': 'kakaemma',
            'password': '1234567'
        })

        self.login_user = json.dumps({
            'email': 'kakaemma@gmail.com',
            'password': '1234567'
        })