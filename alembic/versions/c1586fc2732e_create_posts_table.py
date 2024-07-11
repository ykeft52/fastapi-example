"""create posts table

Revision ID: c1586fc2732e
Revises: 
Create Date: 2024-07-06 05:34:50.004221

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1586fc2732e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table('posts', sa.Column('id',sa.Integer(), nullable =False,primary_key =True),
                     sa.Column('title',sa.String(),nullable =False))


def downgrade() -> None:
    op.drop_table('posts')
