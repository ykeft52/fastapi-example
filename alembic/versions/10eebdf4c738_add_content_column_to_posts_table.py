"""add content column to posts table

Revision ID: 10eebdf4c738
Revises: c1586fc2732e
Create Date: 2024-07-10 07:12:29.102343

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10eebdf4c738'
down_revision: Union[str, None] = 'c1586fc2732e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable =False))


def downgrade() -> None:
    op.drop_column('posts','content')
