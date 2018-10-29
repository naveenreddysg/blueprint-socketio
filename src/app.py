from flask import Flask
from flask_socketio import SocketIO
from configure.register import register_blueprints
from main.sockets import socketio


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
    socketio.init_app(app)
    register_blueprints(app)
    return app


app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app)