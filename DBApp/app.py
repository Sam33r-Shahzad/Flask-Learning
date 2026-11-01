from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Database Object Initialization
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')

    # SQLite Database URI Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'

    # For PostgreSQL (Example):
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flashdb'

    # Initialize DB with App
    db.init_app(app)

    # Register Routes inside factory to avoid Circular Import
    from routes import register_routes
    register_routes(app, db)

    # Setup Flask-Migrate
    migrate = Migrate(app, db)

    return app