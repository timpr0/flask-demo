import unittest
from app.test.base_test import BaseTestCase
from app.main import db
from app.main.model.book import Book

from sqlalchemy.exc import IntegrityError


class TestUserModel(BaseTestCase):  # BaseTestCase = test fixture

    def test_create_book(self):
        """ Test ob die Buch Entität in der Datenbank gespeichert werden kann. """
        # given
        given_book = Book(
            isbn=12345,
            title='Test Buch',
            description='Test Beschreibung',
            author_id=1
        )

        # when
        try:
            db.session.add(given_book)
            db.session.commit()
        except Exception:
            self.fail("Entität konnte nicht gespeichert werden!")

        # then
        # should pass without exception

    def test_integrity_error(self):
        """ Testet die Constraints der Entität """
        # given
        given_book = Book()

        # when
        with self.assertRaises(IntegrityError) as context:

            db.session.add(given_book)
            db.session.commit()

        # then
        self.assertTrue('NOT NULL constraint failed' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
