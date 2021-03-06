"""add config options

Revision ID: f49cafca6dd3
Revises: f44cb612d2fd
Create Date: 2019-09-24 19:08:29.497154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f49cafca6dd3'
down_revision = 'f44cb612d2fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('follow_back', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('follow_timestamp', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('frequency', sa.String(length=128), nullable=True))
    op.add_column('user', sa.Column('like_all', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('like_timestamp', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'like_timestamp')
    op.drop_column('user', 'like_all')
    op.drop_column('user', 'frequency')
    op.drop_column('user', 'follow_timestamp')
    op.drop_column('user', 'follow_back')
    # ### end Alembic commands ###
