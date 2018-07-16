from api.diary import app
from flask_testing import TestCase
import unittest


class TestDevelopmentEnvironment(TestCase):
    """ Test app in development environment"""
    def create_app(self):
        app.config.from_object('instance.config.DevelopmentEnvironment')
        return app

    def test_app_in_development_env(self):
        """ Should return debug is true if debug is enabled"""
        self.assertTrue(app.config['DEBUG'])


class TestProductionEnv(TestCase):
    def create_app(self):
        app.config.from_object('instance.config.ProductionEnvironment')
        return app

    def test_app_in_production(self):
        """ Should return false when debug and testing are off"""
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])


class TestTestingEnv(TestCase):
    def create_app(self):
        app.config.from_object('instance.config.TestingEnvironment')
        return app

    def test_app_in_testing_env(self):
        """ should return true if debug and testing are set to true"""
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])

class TestStagingEnv(TestCase):
    def create_app(self):
        app.config.from_object('instance.config.StagingEnvironment')
        return app

    def test_app_in_staging_env(self):
        """ Check if debug is set to true"""
        self.assertTrue(app.config['DEBUG'])

if __name__ == '__main__':
    unittest.main()