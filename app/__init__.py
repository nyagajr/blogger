from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from config import config_options
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)
simple = SimpleMDE()

def create_app(config_name):

    app = Flask(__name__)


    # app configurations
    app.config.from_object(config_options[config_name])


    # initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
