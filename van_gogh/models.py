"""Module that defines the models that this application will use."""

import datetime

from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, backref

from van_gogh.extensions import db
from van_gogh.schemata import ArtistCreateSchema


class Base(object):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                        nullable=False)

    @classmethod
    def get_by_id(cls, item_id):
        return db.session.query(cls).filter_by(id=item_id).one()


class Artist(db.Model, Base):
    """An Artist that a User can Vote for."""
    name = db.Column(db.Unicode(255), nullable=False, unique=True)

    __tablename__ = 'artists'

    @hybrid_property
    def vote_count(self):
        return len(self.votes)

    @vote_count.expression
    def vote_count_exp(cls):
        return (
            select([func.count(Vote.id)])
            .where(cls.id == Vote.artist_id)
            .label('vote_count')
        )

    @classmethod
    def get_all(cls):
        vote_count = cls.vote_count

        return (
            db.session
            .query(cls, vote_count)
            .order_by(vote_count.desc(), cls.name)
        )

    def add_vote(self):
        vote = Vote(artist=self)
        db.session.add(vote)
        db.session.commit()

    @classmethod
    def add_vote_by_id(cls, artist):
        artist = cls.get_by_id(artist)
        artist.add_vote()

        return artist

    @classmethod
    def create_and_add_vote(cls, data):
        schema = ArtistCreateSchema()
        serialized = schema.load(data).data

        try:
            artist = cls(**serialized)
            db.session.add(artist)
            db.session.commit()
        except IntegrityError:
            artist = db.session.query(cls).filter_by(name=serialized['name'])

        artist.add_vote()

        return artist

class Vote(db.Model, Base):
    """A Vote for a User's favorite artist."""
    artist_id = db.Column(
        db.Integer,
        db.ForeignKey('artists.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False,
    )
    artist = relationship(
        'Artist',
        backref=backref('votes', uselist=True),
    )

    __tablename__ = 'votes'
