import unittest

from mod43.registration import app


class TestAdding(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = "/registration"

    def test_request_OK(self):
        response = self.app.post(self.base_url, data={
            "email": "pochta@dot.com",
            "phone": "9874563211",
            "name": "Игорь",
            "address": "Комарова",
            "index": "188903",
            "comment": "у дверей оставить"
        })
        self.assertEquals(response.status_code, 200)

    def test_email_bad_request(self):
        response = self.app.post(self.base_url, data={
            "email": "pochtadot.com",
            "phone": "9874563211",
            "name": "Игорь",
            "address": "Комарова",
            "index": "188903",
            "comment": "у дверей оставить"
        })
        self.assertEquals(response.status_code, 400)

    def test_phone_bad_request(self):
        response = self.app.post(self.base_url, data={
            "email": "pochtadot.com",
            "phone": "1",
            "name": "Игорь",
            "address": "Комарова",
            "index": "188903",
            "comment": "у дверей оставить"
        })
        self.assertEquals(response.status_code, 400)

    def test_name_bad_request(self):
        response = self.app.post(self.base_url, data={
            "email": "pochtadot.com",
            "phone": "9823448798",
            "name": "",
            "address": "Комарова",
            "index": "188903",
            "comment": "у дверей оставить"
        })
        self.assertEquals(response.status_code, 400)

    def test_address_bad_request(self):
        response = self.app.post(self.base_url, data={
            "email": "pochtadot.com",
            "phone": "9823448798",
            "name": "Игорь",
            "address": "",
            "index": "188903",
            "comment": "у дверей оставить"
        })
        self.assertEquals(response.status_code, 400)

    def test_index_bad_request(self):
        response = self.app.post(self.base_url, data={
            "email": "pochtadot.com",
            "phone": "9823448798",
            "name": "Игорь",
            "address": "Комарова",
            "index": "",
            "comment": "у дверей оставить"
        })
        self.assertEquals(response.status_code, 400)

    def test_without_comment_OK(self):
        response = self.app.post(self.base_url, data={
            "email": "pochta@dot.com",
            "phone": "9823448798",
            "name": "Игорь",
            "address": "Комарова",
            "index": "188903",
            "comment": ""
        })
        self.assertEquals(response.status_code, 200)
