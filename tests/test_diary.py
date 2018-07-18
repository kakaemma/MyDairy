from tests.test_base import BaseClass


class TestDiary(BaseClass):

    def test_add_diary_without_name(self):
        response = self.client.post('/api/v1/diary',
                                    data=self.empty_diary)
        self.assertIn('Missing diary name',
                         response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_diary_successfully(self):
        response = self.client.post('/api/v1/diary',
                                    data=self.new_diary)
        self.assertIn('Diary successfully added', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_diary_with_existing_name(self):
        self.client.post('/api/v1/diary', data=self.new_diary)
        response = self.client.post('/api/v1/diary', data=self.new_diary)
        self.assertIn('Diary name already exists', response.data.decode())
        self.assertEqual(response.status_code, 409)

    def test_get_diaries_on_empty_Diary(self):
        """ Should return no diary entries available"""
        response = self.client.get('/api/v1/diary')
        self.assertIn('No diary entries available', response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_single_diary_on_empty_diary(self):
        """ Should return No diary entries added"""
        response = self.client.get('/api/v1/diary/11')
        self.assertIn('Attempting to retrieve on empty diary',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_single_diary_with_no_id(self):
        """ Should return missing diary id"""
        response = self.client.get('/api/v1/diary/0')
        self.assertIn('Missing diary id', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_single_diary_that_does_not_exist(self):
        """ Should return diary not found and status code 404"""
        self.client.post('/api/v1/diary', data=self.new_diary_2)
        response = self.client.get('/api/v1/diary/45')
        self.assertIn('Diary does not exist', response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_single_diary_successfully(self):
        """ Should return diary retrieved and status code 200"""
        self.client.post('/api/v1/diary', data=self.new_diary_2)
        response = self.client.get('/api/v1/diary/1')
        self.assertIn('Diary retrieved', response.data.decode())
        self.assertEqual(response.status_code, 200)










