from database import db
from flask.ext.bcrypt import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True)
  full_name = db.Column(db.String(120))
  password = db.Column(db.String(120))
  created_at = db.Column(db.DateTime)

  def __init__(self, full_name, email, password):
    self.full_name = full_name
    self.email = email
    self.password = generate_password_hash(password)
    self.created_at = datetime.utcnow()

  def __repr__(self):
    return '<User %r>' % self.full_name

  def username(self):
    return "".join(self.full_name.split(" ")).lower()

  def user_in_fb(self, email):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
      return user
    return None

