"""events

Revision ID: 4b61ef373b7a
Revises: 
Create Date: 2025-04-04 18:21:22.048490

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b61ef373b7a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('coefficient', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('state', sa.Enum('NEW', 'FINISHED_WIN', 'FINISHED_LOSE', name='eventtype'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###
