"""add company to tenders

Revision ID: 44676ff3d1f3
Revises: 6c6b55de44d6
Create Date: 2026-08-08 17:40:14.870226

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "44676ff3d1f3"
down_revision: Union[str, Sequence[str], None] = "6c6b55de44d6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Add company_id temporarily as nullable
    op.add_column(
        "tenders",
        sa.Column("company_id", sa.Integer(), nullable=True)
    )

    # 2. Assign existing tenders to our demo company
    op.execute(
        "UPDATE tenders SET company_id = 3 WHERE company_id IS NULL"
    )

    # 3. Make company_id mandatory
    op.alter_column(
        "tenders",
        "company_id",
        existing_type=sa.Integer(),
        nullable=False
    )

    # 4. Add index
    op.create_index(
        op.f("ix_tenders_company_id"),
        "tenders",
        ["company_id"],
        unique=False
    )

    # 5. Add foreign key
    op.create_foreign_key(
        "fk_tenders_company_id_companies",
        "tenders",
        "companies",
        ["company_id"],
        ["id"]
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_tenders_company_id_companies",
        "tenders",
        type_="foreignkey"
    )

    op.drop_index(
        op.f("ix_tenders_company_id"),
        table_name="tenders"
    )

    op.drop_column(
        "tenders",
        "company_id"
    )