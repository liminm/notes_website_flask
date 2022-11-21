from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] == 'randomstring'
    # local database
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rxmmguileuwnza:f938dc8d8fe0df10d9030a14af700efbde229e48329f151d7b6e801dabb848b9@ec2-52-71-23-11.compute-1.amazonaws.com:5432/d7847n1d0acbgm'
    db = SQLAlchemy(app)


    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/auth')

    from .models import User,Note

    #create_database(app)

    with app.app_context():
        db.create_all()
        print('Created Database!')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))





    return app

# def create_database(app):
#     with app.app_context():
#         if not path.exists('instance/' + DB_NAME):
#             db.create_all()
#             print('Created Database!')
