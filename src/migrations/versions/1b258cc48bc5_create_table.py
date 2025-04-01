"""create_table

Revision ID: 1b258cc48bc5
Revises: 
Create Date: 2025-02-26 00:27:08.913994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b258cc48bc5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('work_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('work_id')
    )
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_table('employee')
    # ### end Alembic commands ###
