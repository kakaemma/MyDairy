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
