"""Module that defines all the routes in this application."""

from flask import jsonify, render_template, request
from flask_classful import FlaskView, route
from marshmallow import ValidationError

from van_gogh import models
from van_gogh.schemata import ArtistSchema


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
    excluded_methods = ['_dump_artists']

    def index(self):
        """Return a list of artists and how many votes for each."""
        return self._dump_artists()

    def post(self):
        """Allow the user to submit a vote for a new artist."""
        data = request.get_json()
        models.Artist.create_and_add_vote(data)

        return self._dump_artists()

    def patch(self, artist_id):
        """Allow the user to vote for an existing artist."""
        models.Artist.add_vote(artist_id)

        return self._dump_artists()

    def _dump_artists(self):
        artists = models.Artist.get_all()
        schema = ArtistSchema()

        return jsonify(schema.dump(artists, many=True).data)


def register(app):
    StaticView.register(app)
    ApiView.register(app)

    def handle_validation_error(exc):
        return jsonify(exc.args[0]), 400

    app.register_error_handler(ValidationError, handle_validation_error)
