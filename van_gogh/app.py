"""App factory for this application."""

from flask import Flask
from werkzeug.datastructures import ImmutableDict

from van_gogh import blueprints, extensions


def create_app(settings=ImmutableDict()):
    # Create and configure the app
    app = Flask(__name__)
    app.config.from_object('van_gogh.settings')

    # Initialize the extensions
    extensions.db.init_app(app)
    extensions.marshmallow.init_app(app)
    # extensions.webpack.init_app(app)

    # Register the routes
    blueprints.register(app)

    return app
