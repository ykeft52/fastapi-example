"""add other few columns to posts table

Revision ID: 0738edb77cfc
Revises: e9c08d1ae85e
Create Date: 2024-07-11 00:59:29.338887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0738edb77cfc'
down_revision: Union[str, None] = 'e9c08d1ae85e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable =False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable =False,server_default=
                                    sa.text('NOW()')))
    


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
