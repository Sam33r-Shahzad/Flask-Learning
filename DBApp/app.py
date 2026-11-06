# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# # Database Object Initialization
# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__, template_folder='templates')

#     # SQLite Database URI Configuration
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'

#     # For PostgreSQL (Example):
#     # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flashdb'

#     # Initialize DB with App
#     db.init_app(app)

#     # Register Routes inside factory to avoid Circular Import
#     from routes import register_routes
#     register_routes(app, db)

#     # Setup Flask-Migrate
#     migrate = Migrate(app, db)

#     return app



from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
    app.secret_key = 'super_secret_key_sample'

    db.init_app(app)

    # Initialize LoginManager & Bcrypt
    login_manager = LoginManager()
    login_manager.init_app(app)

    bcrypt = Bcrypt(app)

    # Load User Callback for Flask-Login
    from models import User
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))

    # Unauthorized access handler (Redirect if not logged in)
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('index'))

    # Register Routes
    from routes import register_routes
    register_routes(app, db, bcrypt)

    migrate = Migrate(app, db)

    return app