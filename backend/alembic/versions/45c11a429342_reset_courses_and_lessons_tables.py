"""Reset courses and lessons tables

Revision ID: 45c11a429342
Revises: a8e37b583be6
Create Date: 2025-06-11 18:21:27.263723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45c11a429342'
down_revision: Union[str, None] = 'a8e37b583be6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


#Solo usar en entornos de desarrollo y prueba, en producción se recomienda tener respaldos antes de usarlo.
def upgrade() -> None:
    """Upgrade schema."""
    op.drop_table("lessons")
    op.drop_table("courses")

    op.create_table(
        "courses",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=1024)),
        sa.Column("instructor", sa.String(length=255), nullable=False)
    )

    op.create_table(
        "lessons",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("video_url", sa.String(length=255), nullable=False),
        sa.Column("course_id", sa.Integer, sa.ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("lessons")
    op.drop_table("courses")
    pass
