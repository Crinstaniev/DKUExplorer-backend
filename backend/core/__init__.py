from flask import Flask
from flask_admin import Admin


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    import core.routes as routes
    from core.admin import admin
    from core.models import db

    app.register_blueprint(routes.bp)
    db.init_app(app)
    admin.init_app(app)

    with app.app_context():
        db.create_all()

    return app
