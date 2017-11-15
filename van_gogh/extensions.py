"""Module that defines extensions for Flask."""

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_webpack import Webpack


db = SQLAlchemy()
marshmallow = Marshmallow()
webpack = Webpack()
