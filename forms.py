from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import Optional

class SearchForm(FlaskForm):
    search_first_name = StringField('First Name', validators=[Optional()])
    search_last_name = StringField('Last Name', validators=[Optional()])
    search_position = StringField('Position', validators=[Optional()])
    district = SelectField('District', choices=[], validators=[Optional()], name="search_district")
    page_limit = SelectField('Page Limit', choices=[('10', '10'), ('25', '25'), ('50', '50'), ('100', '100')], default='10')

