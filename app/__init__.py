from flask import Flask
from app import index
import logging
import config
from logging.handlers import RotatingFileHandler
import logging, logging.config, yaml

class MyApp:
    def __init__(self,config_file):
        self.app = Flask(__name__)

    def setup_logging(self):
        logger = logging.getLogger('werkzeug')
        handler = logging.FileHandler(config.log_file)
        console_handler = logging.StreamHandler()
        logger.addHandler(handler)
        logger.addHandler(console_handler)

    def load_blueprints(self):
        self.app.register_blueprint(index.index_page)

    def run_app(self):
        self.app.run(debug=config.debug_mode)
