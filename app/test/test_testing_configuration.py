from flask import current_app
from flask_testing import TestCase

from manage import app


class TestTestingConfiguration(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is True)
        self.assertTrue(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] is False)
        self.assertTrue(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] is False)
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] is not None)
