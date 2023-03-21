import unittest

from mod52.distance_coding import app


class TestRightCode(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = "distance_coding"

    def test_request_OK(self):
        response = self.app.post(self.base_url, data={
            "code": "print('Hello world!')",
            "time": "5"
        })
        self.assertEqual(response.status_code, 200)

    def test_timeout_is_lower_than_execution_time(self):
        response = self.app.post(self.base_url, data={
            "code": "import time; time.sleep(5)",
            "time": "2"
        })
        self.assertEqual(response.status_code, 400)

    def test_incorrectly_entered_data_in_the_form(self):
        response = self.app.post(self.base_url, data={
            "code": "print('Hello world')",
            "time": "35"
        })
        self.assertEqual(response.status_code, 400)

    def test_unsecure_input(self):
        response = self.app.post(self.base_url, data={
            "code": "from subprocess import run; run(['./kill_the_system.sh'])",
            "time": "2"
        })
        self.assertEqual(response.status_code, 400)
