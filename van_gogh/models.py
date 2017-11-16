"""Module that defines the models that this application will use."""

import datetime

from sqlalchemy import func, select
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, backref

from van_gogh.extensions import db


class Base(object):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                        nullable=False)


class Artist(db.Model, Base):
    """An Artist that a User can Vote for."""
    name = db.Column(db.Unicode(255), nullable=False)

    __tablename__ = 'artists'

    @hybrid_property
    def vote_count(self):
        return self.votes.count()

    @hybrid_property.expression
    def vote_count_exp(cls):
        return (
            select([func(Vote.id)])
            .where(cls.id == Vote.artist_id)
            .label('vote_count')
        )

    @classmethod
    def add_vote(cls, artist_id):
        pass

    @classmethod
    def create_and_add_vote(data):
        pass


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
        cascade='all, delete-orphan'
    )

    __tablename__ = 'votes'
