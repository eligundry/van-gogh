"""Settings for this application."""

import random
import string


# Basic Flask things
DEBUG = True
TESTING = False
SECRET_KEY = ''.join(random.choices(string.ascii_letters + string.digits, k=64))

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:password@postgres:5432/van_gogh'

# Webpack settings
WEBPACK_MANIFEST_PATH = './build/manifest.json'
