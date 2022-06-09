"""empty message

Revision ID: 8570fba4c1ee
Revises: c3829a3bcabd
Create Date: 2022-06-09 16:07:02.821369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8570fba4c1ee'
down_revision = 'c3829a3bcabd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
