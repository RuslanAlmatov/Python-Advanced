import unittest

from mod32.decrypt import decrypt


class TestDecrypt(unittest.TestCase):

    def test_case_with_one_dot(self):
        examples = ["абра-кадабра."]
        for i in examples:
            with self.subTest(i=i):
                self.assertEqual(decrypt(i), "абра-кадабра")

    def test_case_with_two_dots(self):
        examples = ["абраа..-кадабра", "абра--..кадабра"]
        for i in examples:
            with self.subTest(i=i):
                self.assertEqual(decrypt(i), "абра-кадабра")

    def test_case_with_three_dots(self):
        examples = ["абраа..-.кадабра", "абрау...-кадабра"]
        for i in examples:
            with self.subTest(i=i):
                self.assertEqual(decrypt(i), "абра-кадабра")

    def test_case_with_set_of_dots_or_only_dot(self):
        examples = ["абра........", "1.......................", "."]
        for i in examples:
            with self.subTest(i=i):
                self.assertEqual(decrypt(i), "")

    def test_case_with_numbers(self):
        examples = ["1..2.3"]
        for i in examples:
            with self.subTest(i=i):
                self.assertEqual(decrypt(i), "23")
