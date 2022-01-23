from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, EqualTo, Email
 


class CarInfoForm(FlaskForm):
    year = StringField('Year', validators = [DataRequired()])
    make = StringField('Make', validators = [DataRequired()])
    model = StringField("Model", validators = [DataRequired()])
    color = StringField('Color', validators= [DataRequired()])
    image = StringField('img_url')
    submit = SubmitField()