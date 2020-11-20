import unittest
from app.test.base_test import BaseTestCase
from app.main import db
from app.main.model.author import Author

from sqlalchemy.exc import IntegrityError


class TestUserModel(BaseTestCase):  # BaseTestCase = test fixture

    def test_create_author(self):
        """ Test ob die Autor Entität in der Datenbank gespeichert werden kann. """
        # given
        given_author = Author(
            name='test_name',
            last_name='test_last_name'
        )

        # when
        try:
            db.session.add(given_author)
            db.session.commit()
        except Exception:
            self.fail("Entität konnte nicht gespeichert werden!")

        # then
        # should pass without exception

    def test_integrity_error(self):
        """ Testet die Constraints der Entität """
        # given
        given_author = Author()

        # when
        with self.assertRaises(IntegrityError) as context:

            db.session.add(given_author)
            db.session.commit()

        # then
        self.assertTrue('NOT NULL constraint failed' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
