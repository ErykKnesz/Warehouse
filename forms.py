from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired, InputRequired


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = DecimalField('Quantity', validators=[InputRequired()])
    unit = StringField('Unit', validators=[DataRequired()])
    unit_price = DecimalField('Unit Price', validators=[InputRequired()])


class ProductSaleForm(FlaskForm):
    quantity = DecimalField('Quantity', validators=[InputRequired()])