"""Initial database schema

Revision ID: c3ac9b3cc090
Revises: 
Create Date: 2025-07-14 23:21:46.868717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3ac9b3cc090'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('role', sa.Enum('CEO', 'STOREKEEPER', 'SELLER', 'PURCHASER', 'DRIVER', name='userrole'), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('salary', sa.Float(), nullable=True),
    sa.Column('is_paid', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('gradient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fruit_type', sa.String(length=50), nullable=False),
    sa.Column('gradient_type', sa.String(length=50), nullable=False),
    sa.Column('application_date', sa.Date(), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('applied_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['applied_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('quantity', sa.String(length=50), nullable=False),
    sa.Column('fruit_type', sa.String(length=50), nullable=False),
    sa.Column('unit', sa.String(length=20), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('expiry_date', sa.Date(), nullable=True),
    sa.Column('added_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['added_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('recipient_role', sa.Enum('CEO', 'STOREKEEPER', 'SELLER', 'PURCHASER', 'DRIVER', name='userrole'), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('purchaser_id', sa.Integer(), nullable=False),
    sa.Column('supplier_name', sa.String(length=100), nullable=False),
    sa.Column('fruit_type', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.String(length=50), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('purchase_date', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['purchaser_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sale',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('assignment', sa.String(length=100), nullable=True),
    sa.Column('fruit_type', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.String(length=50), nullable=False),
    sa.Column('revenue', sa.Float(), nullable=False),
    sa.Column('sale_date', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock_movement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inventory_id', sa.Integer(), nullable=False),
    sa.Column('movement_type', sa.String(length=10), nullable=False),
    sa.Column('quantity', sa.String(length=50), nullable=False),
    sa.Column('unit', sa.String(length=20), nullable=True),
    sa.Column('remaining_stock', sa.String(length=50), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('added_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['added_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['inventory_id'], ['inventory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock_movement')
    op.drop_table('sale')
    op.drop_table('purchase')
    op.drop_table('message')
    op.drop_table('inventory')
    op.drop_table('gradient')
    op.drop_table('user')
    # ### end Alembic commands ###
