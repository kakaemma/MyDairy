import unittest
from flask import json
from app.views import app
from instance.config import application_config
from app.models import DiaryModel
from app.models import ItemModel
from app.models import UserModel
import jwt
import datetime

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
        self.empty_reset_password = json.dumps({
            'email': '',
            'password': '',
            'new_password': ''
        })
        self.wrong_reset_details = json.dumps({
            'email': 'emma1@gmail.com',
            'password': '1234568',
            'new_password': 'qwertyui'
        })

        self.same_old_password = json.dumps({
            'email': 'kakaemma@gmail.com',
            'password': '1234567',
            'new_password': '1234567'
        })
        self.reset_details = json.dumps({
            'email': 'kakaemma@gmail.com',
            'password': '1234567',
            'new_password': '7654321'
        })

        self.empty_diary = json.dumps({
            'name':''
        })
        self.new_diary = json.dumps({
            'name':'Uganda rally 2018'
        })
        self.new_diary_2 = json.dumps({
            'name':'Uganda rally 2018'
        })
        self.edit_diary = json.dumps({
            'name':'Pearl rally 2018'
        })
        self.empty_desc = json.dumps({
            'desc':''
        })
        self.short_desc = json.dumps({
            'desc':'Andela'
        })
        self.desc = json.dumps({
            'desc':'Andela Uganda cohort 10 boot camp'
        })
        self.desc2 = json.dumps({
            'desc': 'Andela Uganda cohort 10 boot camp week one'
        })

        self.client.post('/api/v1/register',
                                    content_type='application/json',
                                    data=self.user)
        response = self.client.post('/api/v1/login',
                                    content_type='application/json',
                                    data=self.login_user)
        json_data = json.loads(response.data.decode())
        self.token = json_data['token']
        self.header = {'Authorization': self.token}

        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub':7
        }
        self.invalid_token = jwt.encode(
            payload,
            '2018secret',
            algorithm='HS256'
        )
        self.wrong_header = {'Authorization': self.invalid_token}




    def tearDown(self):
        DiaryModel.diary = []
        ItemModel.description = []
        UserModel.user = []

