"""Tests for the models of Van Gogh."""

from van_gogh import models
from van_gogh.extensions import db

def test_create_and_vote_for_artist(faker):
    payload = {'name': faker.bs()}
    artist = models.Artist.create_and_add_vote(payload)

    assert artist.name == payload['name']
    assert artist.vote_count == 1


def test_add_vote_to_existing_artist(artist):
    artist.add_vote()
    assert artist.vote_count == 1


def test_artists_are_returned_in_decending_order_of_votes(faker):
    # Create 5 Artists, each with one more vote than the last
    for vote_count in range(5):
        artist = models.Artist(name=faker.bs())
        db.session.add(artist)

        for _ in range(vote_count + 1):
            db.session.add(models.Vote(artist=artist))

    db.session.commit()

    for idx, artist in enumerate(models.Artist.get_all().limit(5)):
        assert artist.vote_count == 5 - idx
