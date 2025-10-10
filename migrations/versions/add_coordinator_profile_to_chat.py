"""add coordinator profile to chat

Revision ID: add_coordinator_profile
Revises: 
Create Date: 2025-10-10

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add_coordinator_profile'
down_revision = None  # 최신 마이그레이션 ID로 변경 필요

def upgrade():
    # coordinator_profile 컬럼이 없는 경우에만 추가
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [col['name'] for col in inspector.get_columns('chat')]
    
    if 'coordinator_profile' not in columns:
        op.add_column('chat', sa.Column('coordinator_profile', sa.String(length=500), nullable=True))

def downgrade():
    op.drop_column('chat', 'coordinator_profile')

