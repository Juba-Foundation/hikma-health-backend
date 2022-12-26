"""add section, serial_number, and registered_by_provider_id to patients

Revision ID: e7822ef40219
Revises: e778cb1d223e
Create Date: 2022-12-26 00:30:08.075735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e7822ef40219"
down_revision = "e778cb1d223e"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        "ALTER TABLE patients ADD COLUMN section uuid REFERENCES string_ids(id) ON DELETE CASCADE"
    )
    op.execute("ALTER TABLE patients ADD COLUMN serial_number text")
    op.execute("ALTER TABLE patients ADD COLUMN registered_by_provider_id text")


def downgrade():
    op.execute("ALTER TABLE patients DROP COLUMN section")
    op.execute("ALTER TABLE patients DROP COLUMN serial_number")
    op.execute("ALTER TABLE patients DROP COLUMN registered_by_provider_id")
