import unittest

from mod33.accounting_finance import app


class TestAdding(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = "/add/"

    def test_adding_in_storage(self):
        date = "20220218/700"
        response = self.app.get(self.base_url + date)
        response_text = response.data.decode()
        corr_answer = "1000"
        self.assertTrue(corr_answer in response_text)

    def test_add_correct_date(self):
        date = "20221317/800"
        with self.assertRaises(ValueError):
            self.app.get(self.base_url + date)


class TestCalculating(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = "/calculate/"

    def test_calculate_year(self):
        year = "2022"
        response = self.app.get(self.base_url + year)
        response_text = response.data.decode()
        corr_answer = "2400"
        self.assertTrue(corr_answer in response_text)

    def test_calculate_year_and_month(self):
        year_and_month = "2023/2"
        response = self.app.get(self.base_url + year_and_month)
        response_text = response.data.decode()
        corr_answer = "10900"
        self.assertTrue(corr_answer in response_text)

    def test_empty_storage(self):
        year = "2023"
        with self.assertRaises(KeyError):
            self.app.get(self.base_url + year)
