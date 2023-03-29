from app.blueprints import index, error, contact_form


class MyApp:

    def __init__(self, app):
        self.app = app

    def load_blueprints(self):
        self.app.register_blueprint(index.index_page)
        self.app.register_blueprint(error.errors_bp)
        self.app.register_blueprint(contact_form.contact_page)
