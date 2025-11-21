"""add timestamps, task parent/child, roles, estimates

Revision ID: b9fc1d48a108
Revises: 036c0e90030e
Create Date: 2025-11-22 00:14:39.943715
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "b9fc1d48a108"
down_revision: Union[str, Sequence[str], None] = "036c0e90030e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # ---------------------------------------------------------
    # 1️⃣ CREATE ENUM TYPES BEFORE USING THEM
    # ---------------------------------------------------------
    taskpriority = postgresql.ENUM("low", "medium", "high", name="taskpriority")
    taskpriority.create(op.get_bind(), checkfirst=True)

    userrole = postgresql.ENUM("admin", "user", name="userrole")
    userrole.create(op.get_bind(), checkfirst=True)

    # ---------------------------------------------------------
    # 2️⃣ Alter tasks.priority to new ENUM
    # ---------------------------------------------------------
    priority_enum = sa.Enum('LOW', 'MEDIUM', 'HIGH', 'CRITICAL', name="taskpriority")
    priority_enum.create(op.get_bind(), checkfirst=True)

    op.execute(
        "ALTER TABLE tasks ALTER COLUMN priority TYPE taskpriority USING priority::taskpriority"
    )

    # ---------------------------------------------------------
    # 3️⃣ AUTO-GENERATED CHANGES
    # ---------------------------------------------------------
    op.add_column(
        "projects",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.add_column(
        "projects",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.alter_column(
        "projects",
        "description",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        existing_nullable=True,
    )

    op.add_column("tasks", sa.Column("parent_id", sa.Integer(), nullable=True))
    op.add_column("tasks", sa.Column("created_by", sa.Integer(), nullable=True))
    op.add_column("tasks", sa.Column("expected_hours", sa.Float(), nullable=True))
    op.add_column("tasks", sa.Column("actual_hours", sa.Float(), nullable=True))
    op.add_column(
        "tasks",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.add_column(
        "tasks",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.alter_column(
        "tasks",
        "description",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        existing_nullable=True,
    )

    # ❗ removed the duplicate priority alter_column here

    op.create_foreign_key(None, "tasks", "users", ["created_by"], ["id"])
    op.create_foreign_key(None, "tasks", "tasks", ["parent_id"], ["id"])

    op.add_column(
        "users",
        sa.Column(
            "role", sa.Enum("admin", "user", name="userrole"), server_default="user", nullable=False
        ),
    )
    op.add_column(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.add_column(
        "users",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )

    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN is_active
        TYPE BOOLEAN
        USING is_active::BOOLEAN;
        """
    )

    op.drop_column("users", "is_superuser")


def downgrade() -> None:
    """Downgrade schema."""

    # ---------------------------------------------------------
    # 1️⃣ Revert priority ENUM first
    # ---------------------------------------------------------
    op.alter_column(
        "tasks",
        "priority",
        type_=sa.String(),
        existing_type=postgresql.ENUM(name="taskpriority"),
        nullable=True,
    )

    # ---------------------------------------------------------
    # 2️⃣ Drop ENUMs after removing usage
    # ---------------------------------------------------------
    postgresql.ENUM(name="taskpriority").drop(op.get_bind(), checkfirst=True)
    postgresql.ENUM(name="userrole").drop(op.get_bind(), checkfirst=True)

    # ---------------------------------------------------------
    # 3️⃣ Auto-generated reversals
    # ---------------------------------------------------------
    op.add_column("users", sa.Column("is_superuser", sa.INTEGER(), autoincrement=False, nullable=True))
    op.alter_column(
        "users",
        "is_active",
        existing_type=sa.Boolean(),
        type_=sa.INTEGER(),
        nullable=True,
    )
    op.drop_column("users", "updated_at")
    op.drop_column("users", "created_at")
    op.drop_column("users", "role")

    op.drop_constraint(None, "tasks", type_="foreignkey")
    op.drop_constraint(None, "tasks", type_="foreignkey")

    op.alter_column(
        "tasks",
        "description",
        existing_type=sa.Text(),
        type_=sa.VARCHAR(),
        existing_nullable=True,
    )
    op.drop_column("tasks", "updated_at")
    op.drop_column("tasks", "created_at")
    op.drop_column("tasks", "actual_hours")
    op.drop_column("tasks", "expected_hours")
    op.drop_column("tasks", "created_by")
    op.drop_column("tasks", "parent_id")

    op.alter_column(
        "projects",
        "description",
        existing_type=sa.Text(),
        type_=sa.VARCHAR(),
        existing_nullable=True,
    )
    op.drop_column("projects", "updated_at")
    op.drop_column("projects", "created_at")
