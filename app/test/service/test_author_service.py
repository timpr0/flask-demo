import unittest
from unittest.mock import patch

from app.test.base_test import BaseTestCase
from app.main import db
from app.main.model.author import Author
from app.main.service.author_service import get_all_authors
from app.main.utils.exceptions import DatabaseException


class TestUserModel(BaseTestCase):

    def test_get_all_authors_p(self):
        """ Erhalte alle Autoren """
        # given
        given_author = Author(name="vorname", last_name="nachname")
        expected_author = Author(id=1, name="vorname", last_name="nachname")
        expected_author_list = [expected_author]

        # when
        db.session.add(given_author)
        db.session.commit()
        result_list = get_all_authors()

        # them
        self.assertEqual(expected_author_list, result_list, "Die Listen sollten identisch sein.")

    @patch('app.main.service.author_service.Author')  # NICHT app.main.model.author.Author
    def test_get_all_authors_n(self, mock_author):
        """ Testen Custom Exception
            https://docs.python.org/3/library/unittest.mock.html#where-to-patch
        """
        # given
        mock_author.query.all.side_effect = Exception("DB not available")

        # when
        with self.assertRaises(DatabaseException) as context:
            get_all_authors()

        # then
        self.assertIsNotNone(context)


if __name__ == '__main__':
    unittest.main()
