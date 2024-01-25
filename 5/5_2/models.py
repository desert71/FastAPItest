from pydantic import BaseModel
from typing import Optional
from alembic import op
import sqlalchemy as sa

class UserCreate(BaseModel):
    username: str
    email: str
    
class UserReturn(BaseModel):
    username: str
    email: str
    id: Optional[int] = None

# Revision идентифицирует этот миграционный скрипт
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
    )


def downgrade():
    op.drop_table('users')