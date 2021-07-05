# in forms.py of owner. It contains form elements for owner component
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField


# there are 2 add forms now. first under owener and the 2nd under puppy.
class AddForm(FlaskForm):
    owner = StringField("Enter Owner Name: ")
    puppy_id = IntegerField("Enter the ID of the puppy: ")
    submit = SubmitField("Submit Owner")