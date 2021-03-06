from tests.test_base import BaseClass


class TestDiaryDescription(BaseClass):

    def test_add_diary_description_with_no_id(self):
        response = self.client.post('/api/v1/diary/0/item',
                                    content_type='application/json',
                                    data=self.desc,
                                    headers=self.header)
        self.assertIn('Missing diary id', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_description_on_empty_diary(self):
        response = self.client.post('/api/v1/diary/1/item',
                                    content_type='application/json',
                                    data=self.desc,
                                    headers=self.header)
        self.assertIn('Can not add description on empty diary',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_empty_description(self):
        response = self.client.post('/api/v1/diary/1/item',
                                    content_type='application/json',
                                    data=self.empty_desc,
                                    headers=self.header)
        self.assertIn('Missing description', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_short_description(self):
        response = self.client.post('/api/v1/diary/1/item',
                                    content_type='application/json',
                                    data=self.short_desc,
                                    headers=self.header)
        self.assertIn('Description must have\
             a minimum of 10 characters', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_description_on_non_existing_dairy(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.post('/api/v1/diary/2/item',
                                    content_type='application/json',
                                    data=self.desc,
                                    headers=self.header)
        self.assertIn('Attempting to add description\
                 on non existing entry', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_description_successfully(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.post('/api/v1/diary/1/item',
                                    content_type='application/json',
                                    data=self.desc,
                                    headers=self.header)
        self.assertIn('Diary description added', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_edit_diary_description_with_no_id(self):
        response = self.client.put('/api/v1/diary/0/item/0',
                                   content_type='application/json',
                                   data=self.desc,
                                   headers=self.header)
        self.assertIn('Missing id', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_edit_diary_with_empty_description(self):
        response = self.client.put('/api/v1/diary/1/item/1',
                                   content_type='application/json',
                                   data=self.empty_desc,
                                   headers=self.header)
        self.assertIn('Missing description', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_edit_diary_with_short_description(self):
        response = self.client.put('/api/v1/diary/1/item/1',
                                   content_type='application/json',
                                   data=self.short_desc,
                                   headers=self.header)
        self.assertIn('Description must have\
             a minimum of 10 characters', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_edit_diary_on_empty_diary(self):
        response = self.client.put('/api/v1/diary/1/item/1',
                                   content_type='application/json',
                                   data=self.desc,
                                   headers=self.header)
        self.assertIn('Can not edit \
            description on empty diary', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_edit_non_existing_diary_entry(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.put('/api/v1/diary/5/item/1',
                                   content_type='application/json',
                                   data=self.desc2,
                                   headers=self.header)
        self.assertIn('Attempting to modify description\
                 on non existing diary entry', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_edit_description_on_empty_desc(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.put('/api/v1/diary/1/item/1',
                                   content_type='application/json',
                                   data=self.desc2,
                                   headers=self.header)
        self.assertIn('No descriptions added', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_edit_non_existing_description(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        self.client.post('/api/v1/diary/1/item',
                         content_type='application/json',
                         data=self.desc,
                         headers=self.header)
        response = self.client.put('/api/v1/diary/1/item/4',
                                   content_type='application/json',
                                   data=self.desc2,
                                   headers=self.header)
        self.assertIn('Description with \
            that id does not exist', response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_edit_description_with_same_name(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        self.client.post('/api/v1/diary/1/item',
                         content_type='application/json',
                         data=self.desc,
                         headers=self.header)
        response = self.client.put('/api/v1/diary/1/item/1',
                                   content_type='application/json',
                                   data=self.desc,
                                   headers=self.header)
        self.assertIn('Can not edit item with same description',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_edit_description_successfully(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        self.client.post('/api/v1/diary/1/item',
                         content_type='application/json',
                         data=self.desc,
                         headers=self.header)
        self.client.put('/api/v1/diary/1/item/1',
                        content_type='application/json',
                        data=self.desc2,
                        headers=self.header)
        response = self.client.put('/api/v1/diary/1/item/1',
                                   content_type='application/json',
                                   data=self.desc,
                                   headers=self.header)
        self.assertIn('Description changed',
                      response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_descriptions_with_no_id(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        self.client.post('/api/v1/diary/1/item',
                         content_type='application/json',
                         data=self.desc,
                         headers=self.header)
        response = self.client.get('/api/v1/diary/0/item', headers=self.header)
        self.assertIn('Diary id missing', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_description_on_empty_diary(self):
        response = self.client.get('/api/v1/diary/1/item', headers=self.header)
        self.assertIn('Can not retrieve \
            description on empty diary',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_det_description_with_no_description(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        response = self.client.get('/api/v1/diary/1/item', headers=self.header)
        self.assertIn('No descriptions added',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_non_existing_description(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        self.client.post('/api/v1/diary/1/item',
                         content_type='application/json',
                         data=self.desc,
                         headers=self.header)
        response = self.client.get('/api/v1/diary/3/item',
                                   headers=self.header)
        self.assertIn('Attempting to retrieve non existing entry',
                      response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_description_successfully(self):
        self.client.post('/api/v1/diary',
                         content_type='application/json',
                         data=self.new_diary_2,
                         headers=self.header)
        self.client.post('/api/v1/diary/1/item',
                         content_type='application/json',
                         data=self.desc,
                         headers=self.header)
        response = self.client.get('/api/v1/diary/1/item',
                                   headers=self.header)
        self.assertIn('Diary with id',
                      response.data.decode())
        self.assertEqual(response.status_code, 200)
