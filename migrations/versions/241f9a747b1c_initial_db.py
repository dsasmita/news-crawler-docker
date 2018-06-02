"""initial DB

Revision ID: 241f9a747b1c
Revises: 
Create Date: 2018-06-02 03:38:25.287505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '241f9a747b1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('master_news_post',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('tags', sa.Text(), nullable=True),
    sa.Column('category', sa.Text(), nullable=True),
    sa.Column('category_sub', sa.Text(), nullable=True),
    sa.Column('breadcrumb', sa.Text(), nullable=True),
    sa.Column('date_publish', sa.DateTime(), nullable=True),
    sa.Column('image_link', sa.Text(), nullable=True),
    sa.Column('author', sa.Text(), nullable=True),
    sa.Column('meta_description', sa.Text(), nullable=True),
    sa.Column('meta_keyword', sa.Text(), nullable=True),
    sa.Column('meta_content_category', sa.Text(), nullable=True),
    sa.Column('meta_content_category_sub', sa.Text(), nullable=True),
    sa.Column('meta_content_location', sa.Text(), nullable=True),
    sa.Column('meta_content_author', sa.Text(), nullable=True),
    sa.Column('meta_content_editor', sa.Text(), nullable=True),
    sa.Column('meta_content_lipsus', sa.Text(), nullable=True),
    sa.Column('meta_content_type', sa.Text(), nullable=True),
    sa.Column('meta_content_publish_date', sa.DateTime(), nullable=True),
    sa.Column('meta_content_source', sa.Text(), nullable=True),
    sa.Column('meta_content_tag', sa.Text(), nullable=True),
    sa.Column('meta_content_total_words', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('master_news_post')
    # ### end Alembic commands ###