"""add content to post table

Revision ID: 7c2a90f7f70c
Revises: cc77ceafa29c
Create Date: 2023-11-01 18:06:24.292082

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c2a90f7f70c'
down_revision: Union[str, None] = 'cc77ceafa29c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
