"""add extracted text to tender documents

Revision ID: f33cec1c93fb
Revises: 44676ff3d1f3
Create Date: 2026-08-08 21:58:05.851557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f33cec1c93fb'
down_revision: Union[str, Sequence[str], None] = '44676ff3d1f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "tender_documents",
        sa.Column(
            "extracted_text",
            sa.Text(),
            nullable=True
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column(
        "tender_documents",
        "extracted_text"
    )

