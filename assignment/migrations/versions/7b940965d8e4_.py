"""empty message

Revision ID: 7b940965d8e4
Revises: 4d85b439b667
Create Date: 2020-04-17 01:20:39.796025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b940965d8e4'
down_revision = '4d85b439b667'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    op.drop_table('comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('comment', sa.VARCHAR(length=250), nullable=False),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('category_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###
