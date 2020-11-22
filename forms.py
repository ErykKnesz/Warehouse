from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired, InputRequired, ValidationError

'''
def validate_numbers(form, field):
    try:
        return Decimal(field.data)
    except:
        raise ValidationError('This is not a decimal value')
'''

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = DecimalField('Quantity', validators=[InputRequired()])
    unit = StringField('Unit', validators=[DataRequired()])
    unit_price = DecimalField('Unit Price', validators=[InputRequired()])


class ProductSaleForm(FlaskForm):
    quantity = DecimalField('Quantity', validators=[InputRequired()])