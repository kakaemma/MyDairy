from flask_api import FlaskAPI
from instance.config import application_config
import logging
from logging.handlers import RotatingFileHandler


formatter = logging.Formatter(
    "[%ascitime]s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s} "
)
def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(application_config[config_name])
    app.config.from_pyfile('config.py')

    file_handler = RotatingFileHandler(app.config.get('LOGFILE'),
                                  maxBytes=10000000, backupCount=5)
    file_handler.setFormatter(formatter)
    app.logger.setLevel(app.config.get('LEVEL'))
    app.logger.addHandler(file_handler)

    return app
