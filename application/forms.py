from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class TaskForm(FlaskForm):
    task = StringField("Task")
    completed = BooleanField("Completed")
    submit = SubmitField("Submit")