"""Initial migrations with the artists and votes tables.

Revision ID: d9a0e4d3ac31
Revises:
Create Date: 2017-11-16 00:00:31.573770

"""

import datetime

from alembic import op
import sqlalchemy as sa
from flask import current_app


# revision identifiers, used by Alembic.
revision = 'd9a0e4d3ac31'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    artists_table = op.create_table(
        'artists',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Unicode(255), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name', name='uq_artists_name'),
    )
    op.create_table(
        'votes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('artist_id', sa.Integer(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(
            ['artist_id'],
            ['artists.id'],
            name='fk_artists_votes',
            onupdate='CASCADE',
            ondelete='CASCADE',
        ),
    )

    if not current_app.config['TESTING']:
        now = datetime.datetime.utcnow()

        op.bulk_insert(artists_table, [
            {'name': 'Marcel Eichner', 'created': now},
            {'name': 'Jeff Elrod', 'created': now},
            {'name': 'Awol Erizku', 'created': now},
            {'name': 'Hoosen', 'created': now},
            {'name': 'Zak Prekop', 'created': now},
            {'name': 'Julie Oppermann', 'created': now},
            {'name': 'David Ostrowski', 'created': now},
            {'name': 'Christian Rosa', 'created': now},
            {'name': 'Lucien Smith', 'created': now},
        ])


def downgrade():
    op.drop_table('votes')
    op.drop_table('artists')
