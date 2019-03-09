"""empty message

Revision ID: a5f2f5be59cf
Revises: 
Create Date: 2019-03-02 09:41:05.301987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5f2f5be59cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.String(length=255), nullable=False))
    op.create_unique_constraint(None, 'user', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'name')
    # ### end Alembic commands ###