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
        response = self.client.get('/api/v1/diary')
        self.assertIn('No diary entries available', response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_single_diary_on_empty_diary(self):
        response = self.client.get('/api/v1/diary/11')
        self.assertIn('No diary entries added', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_single_diary_with_no_id(self):
        response = self.client.get('/api/v1/diary/0')
        self.assertIn('Missing diary id', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_single_diary_that_does_not_exist(self):
        self.client.post('/api/v1/diary', data=self.new_diary_2)
        response = self.client.get('/api/v1/diary/45')
        self.assertIn('Diary does not exist', response.data.decode())
        self.assertEqual(response.status_code, 404)





