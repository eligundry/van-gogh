"""Schemata for Van Gogh."""

from marshmallow import fields
from marshmallow.validate import Length
from werkzeug.datastructures import ImmutableDict

from van_gogh.extensions import marshmallow


REQUIRED = ImmutableDict({
    'required': True,
    'allow_none': False,
})

STR_REQUIRED = ImmutableDict({
    'required': True,
    'allow_none': False,
    'validate': Length(min=1, max=255)
})

class Base(marshmallow.Schema):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # I want to raise always
        self.strict = True


class ArtistSchema(Base):
    id = fields.Integer(**REQUIRED)
    name = fields.String(**STR_REQUIRED)
    vote_count = fields.Integer(**REQUIRED)


class ArtistCreateSchema(Base):
    name = fields.String(**STR_REQUIRED)
