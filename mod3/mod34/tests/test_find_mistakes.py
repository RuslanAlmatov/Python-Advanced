import unittest

from mod34.find_mistakes import Person


class TestFindMistakes(unittest.TestCase):
    def test_person(self):
        function_res = Person("Алексей", 2003, "Комарова 777")
        self.assertTrue(function_res)

    def test_get_age(self):
        age = 18
        human = Person("Алексей", 2005, "Комарова 322")
        function_res = human.get_age()
        self.assertEqual(age, function_res)

    def test_get_name(self):
        name = "Владимир"
        human = Person("Владимир", 1988, "Карла Маркса 23")
        function_res = human.get_name()
        self.assertEqual(function_res, name)

    def test_set_name(self):
        name = "Алексей"
        human = Person("Владимир", 2000, "Советская 97")
        human.set_name("Алексей")
        function_res = human.get_name()
        self.assertEqual(function_res, name)

    def test_set_adress(self):
        adress = "Комсомольская 10"
        human = Person("Дмитрий", 2002, "Гагарина 10")
        human.set_address("Комсомольская 10")
        function_res = human.get_address()
        self.assertEqual(function_res, adress)

    def test_get_adress(self):
        adress = "Мира 20"
        human = Person("Пётр", 2010, "Мира 20")
        function_res = human.get_address()
        self.assertEqual(function_res, adress)

    def test_is_homeless_True(self):
        flag = True
        human = Person("Роман", 1977)
        function_res = human.is_homeless()
        self.assertEqual(function_res, flag)

    def test_is_homeless_False(self):
        flag = False
        human = Person("Роман", 1977, "Куйбышева 64")
        function_res = human.is_homeless()
        self.assertEqual(function_res, flag)
