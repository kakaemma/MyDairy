from tests.test_base import BaseClass


class TestDiaryDescription(BaseClass):

    def test_add_diary_description_with_no_id(self):
        response = self.client.post('/api/v1/diary/0/item', data=self.desc)
        self.assertIn('Missing diary id', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_description_on_empty_diary(self):
        response = self.client.post('/api/v1/diary/1/item', data=self.desc)
        self.assertIn('Can not add description on empty diary',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_empty_description(self):
        response = self.client.post('/api/v1/diary/1/item', data=self.empty_desc)
        self.assertIn('Missing description', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_short_description(self):
        response = self.client.post('/api/v1/diary/1/item', data=self.short_desc)
        self.assertIn('Description must have\
             a minimum of 10 characters', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_description_on_non_existing_dairy(self):
        self.client.post('/api/v1/diary', data=self.new_diary_2)
        response = self.client.post('/api/v1/diary/2/item', data=self.desc)
        self.assertIn('Attempting to add description\
                 on non existing entry', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_description_successfully(self):
        self.client.post('/api/v1/diary', data=self.new_diary_2)
        response = self.client.post('/api/v1/diary/1/item', data=self.desc)
        self.assertIn('Diary description added', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_edit_diary_description_with_no_id(self):
        response = self.client.put('/api/v1/diary/0/item/0', data=self.desc)
        self.assertIn('Missing id', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_edit_diary_with_empty_description(self):
        response = self.client.put('/api/v1/diary/1/item/1', data=self.empty_desc)
        self.assertIn('Missing description', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_edit_diary_with_short_description(self):
        response = self.client.put('/api/v1/diary/1/item/1', data=self.short_desc)
        self.assertIn('Description must have\
             a minimum of 10 characters', response.data.decode())
        self.assertEqual(response.status_code, 400)
























