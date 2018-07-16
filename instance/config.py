#instance/config.py

import os


class MainConfiguration(object):
    """ Parent configuration class"""
    DEBUG = False
    CSRF = True


class DevelopmentEnvironment(MainConfiguration):
    """ Configurations for development"""
    DEBUG = True

class TestingEnvironment(MainConfiguration):
    """ Configurations for Testing environment"""
    DEBUG = True
    TESTING = True

class StagingEnvironment(MainConfiguration):
    """ Configurations for staging environment"""
    DEBUG = True

class ProductionEnvironment(MainConfiguration):




