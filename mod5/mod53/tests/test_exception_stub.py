import unittest

import pytest

from mod53.exception_stub import BlockError


class TestExceptionStub(unittest.TestCase):
    def test_ignore_error(self):
        err_types = {ZeroDivisionError, TypeError}
        with BlockError(err_types):
            a = 1 / 0
        print('Выполнено без ошибок')

    def test_raise_error(self):
        err_types = {ZeroDivisionError}
        with pytest.raises(TypeError):
            with BlockError(err_types):
                a = 1 / '0'
            print('Выполнено без ошибок')

    def test_ignore_inner_error(self):
        outer_err_types = {TypeError}
        with BlockError(outer_err_types):
            inner_err_types = {ZeroDivisionError}
            with BlockError(inner_err_types):
                a = 1 / '0'
            print('Внутренний блок: выполнено без ошибок')
        print('Внешний блок: выполнено без ошибок')

    def test_ignore_sub_error(self):
        err_types = {Exception}
        with BlockError(err_types):
            try:
                a = 1 / '0'
            except TypeError:
                pass
            print('Выполнено без ошибок')
