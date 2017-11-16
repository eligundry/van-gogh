"""Fixtures for the tests of van-gogh."""

import flask_migrate
import pytest

from faker import Faker
from fleaker.testing import FlaskClient, Response

from van_gogh import models
from van_gogh.app import create_app
from van_gogh.extensions import db


@pytest.fixture(scope='session', autouse=True)
def app():
    settings = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': (
            'postgres://postgres:password@postgres:5432/van_gogh_test'
        ),
    }
    app_ = create_app(settings=settings)

    app_.test_client_class = FlaskClient
    app_.response_class = Response

    # Migrate the database up
    with app_.app_context():
        flask_migrate.upgrade()

    yield app_

    # Destroy the database
    with app_.app_context():
        flask_migrate.downgrade()


@pytest.fixture(scope='session')
def faker():
    faker_ = Faker()
    return faker_


@pytest.fixture
def artist(faker):
    artist = models.Artist(name=faker.bs())
    db.session.add(artist)
    db.session.commit()

    return artist
