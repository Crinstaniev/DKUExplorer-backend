from flask import Flask
from flask_admin import Admin
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    import core.routes as routes
    from core.admin import admin
    from core.models import db
    from core.utils.extensions import cors

    app.register_blueprint(routes.bp)
    db.init_app(app)
    admin.init_app(app)
    cors.init_app(app)

    with app.app_context():
        db.create_all()

    return app
