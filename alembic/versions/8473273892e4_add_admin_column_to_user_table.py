"""add admin column to user table

Revision ID: 8473273892e4
Revises: cd0fccd6f978
Create Date: 2022-06-08 06:14:43.011893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8473273892e4'
down_revision = 'cd0fccd6f978'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column(
        'email_verified', sa.Boolean, nullable=True))
    op.execute("UPDATE users SET email_verified = false")
    op.alter_column('users', 'email_verified', nullable=False)


def downgrade():
    pass
