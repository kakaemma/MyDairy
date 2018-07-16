from tests.test_base import BaseClass


class TestAuthentication(BaseClass):

    def test_index_rout(self):
        """ Test response for title in the index page """
        response = self.client.get('/')
        self.assertIn('Welcome to My Diary', response.data.decode())

    def test_registration_with_no_values(self):
        """ Test registration with missing values"""
        response = self.client.post('/api/v1/register', data=self.empty_reg)
        self.assertIn('Missing values', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_registration_with_invalid_email(self):
        """ Test should return invalid email address"""
        response = self.client.post('api/v1/register',
                                    data=self.invalid_email)
        self.assertIn('Invalid email address', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_registration_with_short_password(self):
        """ Should return password too short"""
        response = self.client.post('api/v1/register',
                                    data=self.short_password)
        self.assertIn('Password too short', response.data.decode())
        self.assertEqual(response.status_code, 422)

    def test_registration_with_existing_email(self):
        """ Should return conflict email already exists"""
        self.client.post('api/v1/register',
                         data=self.user)
        response = self.client.post('api/v1/register',
                                    data=self.user)
        self.assertIn('Email already exists', response.data.decode())
        self.assertEqual(response.status_code, 409)


