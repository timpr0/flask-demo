from flask_testing import TestCase

from manage import app


class TestProductionConfiguration(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is False)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] is not None)
