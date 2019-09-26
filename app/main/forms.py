from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField, SubmitField

class SettingsForm(FlaskForm):
    frequency = SelectField('Frequency', choices=[('every', 'Every Hour'), ('even', 'Even Hours'), ('odd', 'Odd Hours'), ('4', 'Every 4 Hours'), ('6', 'Every 6 Hours'), ('8', 'Every 8 Hours'), ('12', 'Every 12 Hours')])
    like_all = BooleanField('Like all retweets?')
    follow_back = BooleanField('Follow everyone who follows you?')

    submit = SubmitField('Save')


    