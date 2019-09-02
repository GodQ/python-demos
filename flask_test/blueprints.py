from simple import bp as simple_bp
from model_test import bp as model_bp


def register_blueprints(app):
    app.register_blueprint(simple_bp)
    app.register_blueprint(model_bp)
