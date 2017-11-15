"""Module that defines all the routes in this application."""

from flask import render_template
from flask_classful import FlaskView, route


class StaticView(FlaskView):
    trailing_slash = False
    route_base = '/'

    @route('/', defaults={'path': ''})
    @route('/<path:path>')
    def index(self, path):
        return render_template('index.html')


class ApiView(FlaskView):
    trailing_slash = False
    route_base = '/api/artists'

    def index(self):
        """Return a list of artists and how many votes for each."""

    def post(self):
        """Allow the user to submit a vote for an existing artist or new one."""


def register(app):
    StaticView.register(app)
    ApiView.register(app)
