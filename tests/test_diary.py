from tests.test_base import BaseClass


class TestDiary(BaseClass):

    def test_add_diary_without_name(self):
        response = self.client.post('/api/v1/diary',
                                    content_type='application/json',
                                    data=self.empty_diary,
                                    headers=self.header)
        self.assertIn('Missing diary name',
                         response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_diary_without_token(self):
        """ Should return there is no token"""
        response = self.client.post('/api/v1/diary',
                                    content_type='application/json',
                                    data=self.empty_diary)
        self.assertIn('There is no token',
                         response.data.decode())
        self.assertEqual(response.status_code, 401)


    def test_add_diary_with_no_json(self):
        """ Return content-type not json"""
        response = self.client.post('/api/v1/diary',
                                    content_type='text/plain',
                                    data=self.new_diary,
                                    headers=self.header)
        self.assertIn('Content-Type not specified as application/json',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_wrong_token(self):
        """ Return invalid token"""
        response = self.client.post('/api/v1/diary',
                                    content_type='application/json',
                                    data=self.new_diary,
                                    headers=self.wrong_header)
        self.assertIn('Mismatching or wrong token', response.data.decode())
        self.assertEqual(response.status_code, 400)


    def test_add_diary_successfully(self):
        response = self.client.post('/api/v1/diary',
                                    content_type='application/json',
                                    data=self.new_diary,
                                    headers=self.header)
        self.assertIn('Diary successfully added', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_diary_with_existing_name(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header)
        response = self.client.post('/api/v1/diary',
                                    content_type='application/json',
                                    data=self.new_diary,
                                    headers=self.header)
        self.assertIn('Diary name already exists', response.data.decode())
        self.assertEqual(response.status_code, 409)

    def test_get_diaries_on_empty_Diary(self):
        """ Should return no diary entries available"""
        response = self.client.get('/api/v1/diary', headers=self.header)
        self.assertIn('No diary entries available', response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_diaries_successfully(self):
        """ Should return my diary entries"""
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header)
        response = self.client.get('/api/v1/diary', headers=self.header)
        self.assertIn('My Diary entries', response.data.decode())
        self.assertEqual(response.status_code, 200)


    def test_get_single_diary_on_empty_diary(self):
        """ Should return No diary entries added"""
        response = self.client.get('/api/v1/diary/11', headers=self.header)
        self.assertIn('Attempting to retrieve on empty diary',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_single_diary_with_no_id(self):
        """ Should return missing diary id"""
        response = self.client.get('/api/v1/diary/0', headers=self.header)
        self.assertIn('Missing diary id', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_single_diary_that_does_not_exist(self):
        """ Should return diary not found and status code 404"""
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.get('/api/v1/diary/45', headers=self.header)
        self.assertIn('Diary does not exist', response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_single_diary_successfully(self):
        """ Should return diary retrieved and status code 200"""
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.get('/api/v1/diary/1', headers=self.header)
        self.assertIn('Diary retrieved', response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_modify_diary_on_empty_diary(self):
        response = self.client.put('/api/v1/diary/1',
                                   content_type='application/json',
                                   data=self.new_diary_2,
                                   headers=self.header)
        self.assertIn('empty diary', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_modify_diary_with_empty_name(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.put('/api/v1/diary/1',
                                   content_type='application/json',
                                   data=self.empty_diary,
                                   headers=self.header)
        self.assertIn('Missing diary name', response.data.decode())
        self.assertEqual(response.status_code, 422)

    def test_modify_diary_with_no_id(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.put('/api/v1/diary/0',
                                   content_type='application/json',
                                   data=self.new_diary_2,
                                   headers=self.header)
        self.assertIn('Missing diary id', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_modify_diary_with_wrong_id(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.put('/api/v1/diary/2',
                                   content_type='application/json',
                                   data=self.new_diary_2,
                                   headers=self.header)
        self.assertIn('No diary matches the supplied id', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_modify_diary_with_same_name(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.put('/api/v1/diary/1',
                                   content_type='application/json',
                                   data=self.new_diary_2,
                                   headers=self.header)
        self.assertIn('Can not edit diary with', response.data.decode())
        self.assertEqual(response.status_code, 409)

    def test_modify_diary_successfully(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.put('/api/v1/diary/1',
                                   content_type='application/json',
                                   data=self.edit_diary,
                                   headers=self.header)
        self.assertIn('Diary successfully modified', response.data.decode())
        self.assertEqual(response.status_code, 200)