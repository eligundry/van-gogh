"""Settings for this application."""

import random
import string


# Basic Flask things
DEBUG = False
TESTING = False
SECRET_KEY = ''.join(random.choices(string.ascii_letters + string.digits, k=64))

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:password@postgres:5432/van_gogh'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Webpack settings
WEBPACK_MANIFEST_PATH = './build/manifest.json'
WEBPACK_ASSETS_URL = '../frontend'
