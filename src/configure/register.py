from main import sockets


def register_blueprints(app):
    app.register_blueprint(sockets.blueprint)
