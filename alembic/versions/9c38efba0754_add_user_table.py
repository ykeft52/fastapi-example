"""add user table

Revision ID: 9c38efba0754
Revises: 10eebdf4c738
Create Date: 2024-07-10 07:19:02.870553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c38efba0754'
down_revision: Union[str, None] = '10eebdf4c738'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('email',sa.String(),unique =True,nullable =False),
                    sa.Column('password',sa.String(),nullable =False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'),nullable =False),
                              
                              )
                    
                    
                    
                    


def downgrade() -> None:
    op.drop_table('users')
