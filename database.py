# -*- coding:utf-8 -*-

#--- SQLALCHEMY SUPPORT

# uncomment for sqlalchemy support
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def drop_all():
  db.drop_all()


def create_all():
  db.create_all()

def seed_db():
  drop_all()
  create_all()

  from app.models.user import User
  user = User('user', 'email@gmail.com', 'testing')
  db.session.add(user)
  db.session.commit()
  




def remove_session():
  db.session.remove()

#--- SQLALCHEMY SUPPORT END
