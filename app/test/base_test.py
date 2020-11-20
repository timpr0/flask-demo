from flask_testing import TestCase
from app.main import db
from manage import app


class BaseTestCase(TestCase):

    def create_app(self):
        """ Erstellt anhand der Test-Konfiguration eine FlaskApp """
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        """ Wird vor jeder Methode ausgeführt """
        db.create_all()
        db.session.commit()

    def tearDown(self):
        """ Wird nach jeder Methode ausgeführt """
        db.session.remove()
        db.drop_all()
