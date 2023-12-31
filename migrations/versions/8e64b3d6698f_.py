"""empty message

Revision ID: 8e64b3d6698f
Revises: a07854d61c06
Create Date: 2023-10-06 11:56:16.502258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e64b3d6698f'
down_revision = 'a07854d61c06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stats', schema=None) as batch_op:
        batch_op.drop_column('field_goal_percentage')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('field_goal_percentage', sa.FLOAT(), server_default=sa.text("'0'"), nullable=True))

    # ### end Alembic commands ###
