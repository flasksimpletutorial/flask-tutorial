"""empty message

Revision ID: 6b45f402d522
Revises: ffc15323d1b4
Create Date: 2017-12-08 18:30:49.817984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b45f402d522'
down_revision = 'ffc15323d1b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('commenter_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['commenter_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'commenter_id')
    # ### end Alembic commands ###
