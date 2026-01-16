"""create inventory module

Revision ID: 9f9d78e641b1
Revises: 3076d51d119d
Create Date: 2026-01-05 11:27:23.363867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f9d78e641b1'
down_revision: Union[str, Sequence[str], None] = '3076d51d119d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "warehouses",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("code", sa.String(50), nullable= False),
        sa.Column("name", sa.String(255), nullable= False),
        sa.Column("location", sa.String(255)),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text('true')),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index("ix_warehouses_code", "warehouses", ["code"], unique=True),    

    op.create_table(
        "inventories",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("product_id", sa.Integer, nullable=False),
        sa.Column("warehouse_id", sa.Integer, nullable=False),
        sa.Column("quantity", sa.Integer, server_default='0'),
        sa.Column("reserved_quantity", sa.Integer, server_default='0'),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now()),
        # Đảm bảo mỗi sản phẩm trong mỗi kho chỉ có một bản ghi
        sa.UniqueConstraint("product_id", "warehouse_id", name="uq_invetory_product_warehouse"),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"], ondelete="CASCADE"), 
        sa.ForeignKeyConstraint(["warehouse_id"], ["warehouses.id"], ondelete="CASCADE"),
    )

    op.create_table(
        "stock_movements",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("product_id", sa.Integer, nullable=False),
        sa.Column("warehouse_id", sa.Integer, nullable=False),
        sa.Column("movement_type", sa.String(50), nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        
        sa.Column("ref_type", sa.String(50)),
        sa.Column("ref_id", sa.Integer),

        sa.Column("note" , sa.String(255)),

        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
        # Foreign key constraints
        sa.ForeignKeyConstraint(["product_id"], ["products.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["warehouse_id"], ["warehouses.id"], ondelete="CASCADE"),
    )
    op.create_index("ix_stock_movements_product_id", "stock_movements", ["product_id"]),
    op.create_index("ix_stock_movements_warehouse_id", "stock_movements", ["warehouse_id"]),
    op.create_index("ix_stock_movements_created_at", "stock_movements", ["created_at"]),


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("ix_stock_movements_created_at", table_name="stock_movements")
    op.drop_index("ix_stock_movements_warehouse_id", table_name="stock_movements")
    op.drop_index("ix_stock_movements_product_id", table_name="stock_movements")
    op.drop_table("stock_movements")

    op.drop_table("inventories")

    op.drop_index("ix_warehouses_code", table_name="warehouses")
    op.drop_table("warehouses")