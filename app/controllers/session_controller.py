from flask import render_template, request, redirect, url_for
from flask.ext.wtf import Form 
from wtforms import TextField,PasswordField,validators

class LoginForm(Form):
  email = TextField("Email")
  password = PasswordField("Password")
  def validate(self):
    return True

class SignupForm(Form):
  email = TextField("Email", [validators.Length(min=6, max=35), validators.Email()])
  password = PasswordField("Password",[validators.Required()])
  full_name = TextField("Full Name", [validators.Length(min=3, max=35)])

class SessionController:
  @classmethod
  def signin(self):
    form = LoginForm(request.form)
    if form.validate_on_submit():
      return redirect(url_for("index"))
    return render_template('signin.html', form=form)

  @classmethod
  def signup(self):
    form = SignupForm()
    if form.validate_on_submit():
      return redirect(url_for("index"))
    return render_template('signup.html', form=form)
