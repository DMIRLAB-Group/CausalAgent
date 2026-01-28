"""change_content_column_to_mediumtext

Revision ID: d876b980dc9a
Revises: 9359bc171e66
Create Date: 2025-11-27 12:10:02.508036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd876b980dc9a'
down_revision: Union[str, Sequence[str], None] = '9359bc171e66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
        ALTER TABLE chat_messages 
        MODIFY COLUMN content MEDIUMTEXT NOT NULL 
        COMMENT '消息内容（纯文本或简单JSON）'
    """)

def downgrade():
    op.execute("""
        ALTER TABLE chat_messages 
        MODIFY COLUMN content TEXT NOT NULL 
        COMMENT '消息内容（纯文本或简单JSON）'
    """)