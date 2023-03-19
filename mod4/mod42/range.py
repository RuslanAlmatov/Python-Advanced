import math

from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError, Optional


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        data = field.data
        if (data is None and math.isnan(data)) and (min < data) and (max > data):
            raise ValidationError(message)
        return

    return _number_length


class NumberLength:
    def __init__(self, min=None, max=None, message=None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        data = field.data
        if (data is None and math.isnan(data)) and (self.min < data) and (self.max >data):
            raise ValidationError(self.message)
        return
