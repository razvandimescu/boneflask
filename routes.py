from app.controllers.main_controller import MainController
from app.controllers.session_controller import SessionController

def add_routes(app):
  app.add_url_rule('/', 'index', MainController.index)
  app.add_url_rule('/signup', 'signup', SessionController.signup, methods=["GET", "POST"])
  app.add_url_rule('/signin', 'signin', SessionController.signin, methods=["GET", "POST"])
  app.add_url_rule('/signout', 'signout', MainController.index)
