from flask import render_template
from flask.ext.wtf import Form 
from wtforms import TextField, ValidationError, SubmitField

class ExampleForm(Form):
  field1 = TextField("First Field", description="AHAH")
  submit_button = SubmitField("Submit Form")
  def validate_hidden_field(form, field):
    raise ValidationError("Always Wronk")

class MainController:
  @classmethod
  def index(self):
    return render_template('index.html')
