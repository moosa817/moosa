from app.blueprints import index, error, contact_form
import logging
import config


class MyApp:

    def __init__(self, app):
        self.app = app

    def setup_logging(self):
        logger = logging.getLogger('werkzeug')
        handler = logging.FileHandler(config.log_file)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        console_handler = logging.StreamHandler()
        logger.addHandler(handler)
        logger.addHandler(console_handler)

    def load_blueprints(self):
        self.app.register_blueprint(index.index_page)
        self.app.register_blueprint(error.errors_bp)

    def run_app(self):
        debug_mode = True if str(config.debug_mode) == 'True' else False
        self.app.run(debug=debug_mode)
