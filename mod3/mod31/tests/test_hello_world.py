import unittest
from freezegun import freeze_time

from mod31.hello_world import app


class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    @freeze_time("2023-03-01")
    def test_can_get_weekday(self):
        username = "username"
        weekday = "Хорошей среды"
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    def test_can_get_incorrect_username(self):
        username = "Хорошей среды"
        with self.assertRaises(ValueError):
            self.app.get(self.base_url + username)

