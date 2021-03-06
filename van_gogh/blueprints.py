"""Module that defines all the routes in this application."""

import os

from flask import current_app, jsonify, render_template, request
from flask_classful import FlaskView, route
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from van_gogh import models
from van_gogh.schemata import ArtistSchema


FRONTEND = os.path.join('opt', 'van_gogh', 'frontend', 'build')


def dump_artists():
    artists = models.Artist.get_all()
    schema = ArtistSchema()

    return {
        'artists': schema.dump(artists, many=True).data,
        'total_votes': models.Vote.query.count(),
    }


class StaticView(FlaskView):
    trailing_slash = False
    route_base = '/'

    @route('', defaults={'path': 'index.html'})
    @route('/<path:path>')
    def index(self, path):
        return render_template('index.html', artists=dump_artists())


class ApiView(FlaskView):
    trailing_slash = False
    route_base = '/api/artists'

    def index(self):
        """Return a list of artists and how many votes for each."""
        return jsonify(dump_artists())

    def post(self):
        """Allow the user to submit a vote for a new artist."""
        data = request.get_json()
        models.Artist.create_and_add_vote(data)

        return jsonify(dump_artists()), 201

    def patch(self, artist_id):
        """Allow the user to vote for an existing artist."""
        models.Artist.add_vote_by_id(artist_id)

        return jsonify(dump_artists())


def register(app):
    StaticView.register(app)
    ApiView.register(app)

    def handle_validation_error(exc):
        return jsonify(exc.args[0]), 400

    def handle_bad_request(exc):
        return jsonify({"error": "Fix your request"}), 400

    def handle_generic(exc):
        return jsonify({"error": "Something went wrong!"}), 500

    app.register_error_handler(ValidationError, handle_validation_error)
    app.register_error_handler(BadRequest, handle_bad_request)

    if not app.config['DEBUG']:
        app.register_error_handler(Exception, handle_generic)
