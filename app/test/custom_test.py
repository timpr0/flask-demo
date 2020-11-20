from unittest import TestCase


class CustomTestCase(TestCase):

    def setUp(self) -> None:
        """ Wird vor jeder Methode ausgeführt """

    def tearDown(self) -> None:
        """ Wird nach jeder Methode ausgeführt """

    @classmethod
    def setUpClass(cls) -> None:
        """ Wird vor der Testklasse ausgefühert """

    @classmethod
    def tearDownClass(cls) -> None:
        """ Wird nach der Testklasse ausgeführt """
