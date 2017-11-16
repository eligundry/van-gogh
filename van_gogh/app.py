"""App factory for this application."""

from flask import Flask
from werkzeug.datastructures import ImmutableDict

from van_gogh import blueprints, extensions


def create_app(settings=ImmutableDict()):
    """Application factory for Van Gogh.

    Keyword Args:
        settings (dict): The settings to override for a custom app.

    Returns:
        flask.Flask: The app, ready for use!

    """
    # Create and configure the app
    app = Flask(__name__)
    app.config.from_object('van_gogh.settings')
    app.config.from_mapping(settings)

    # Initialize the extensions
    extensions.db.init_app(app)
    extensions.marshmallow.init_app(app)
    extensions.migrate.init_app(app, extensions.db)
    # extensions.webpack.init_app(app)

    # Register the routes
    blueprints.register(app)

    return app
