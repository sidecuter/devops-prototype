"""Initial

Revision ID: 12bcd98b52a1
Revises: 
Create Date: 2024-12-21 02:22:39.192732

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '12bcd98b52a1'
down_revision = None
branch_labels = None
depends_on = None


def data_upgrades():
    """Add any optional data upgrade migrations here!"""

    t_supplier = sa.sql.table(
        'suppliers',
        sa.sql.column('id', sa.Integer),
        sa.sql.column('name', sa.String),
        sa.sql.column('inn', sa.String),
        sa.sql.column('legal_address', sa.String),
        sa.sql.column('bank_address', sa.String),
        sa.sql.column('bank_account_number', sa.String)
    )
    t_mu = sa.sql.table(
        'measurement_units',
        sa.sql.column('id', sa.Integer),
        sa.sql.column('unit', sa.String)
    )
    t_materials = sa.sql.table(
        'materials',
        sa.sql.column('id', sa.Integer),
        sa.sql.column('class_code', sa.String),
        sa.sql.column('group_code', sa.String),
        sa.sql.column('name', sa.String),
        sa.sql.column('measurement_unit_code', sa.Integer)
    )
    t_su = sa.sql.table(
        'storage_units',
        sa.sql.column('order_number', sa.Integer),
        sa.sql.column('date', sa.DateTime),
        sa.sql.column('supplier_code', sa.Integer),
        sa.sql.column('balance_account', sa.String),
        sa.sql.column('document_code', sa.String),
        sa.sql.column('document_number', sa.String),
        sa.sql.column('material_code', sa.Integer),
        sa.sql.column('quantity_received', sa.Integer),
        sa.sql.column('unit_price', sa.Float)
    )

    op.bulk_insert(t_supplier,
                   [
                        {
                           'id': 1,
                           'name': 'ООО Навоз',
                           'inn': '123456789012',
                           'legal_address': 'Москва, ул. Ленина, д. 1',
                           'bank_address': 'Москва, ул. Пушкина, д. 2',
                           'bank_account_number': '123456789012'
                        },
                        {
                           'id': 2,
                           'name': 'ЗАО Стройматериалы',
                           'inn': '987654321098',
                           'legal_address': 'Санкт-Петербург, ул. Невский, д. 3',
                           'bank_address': 'Санкт-Петербург, ул. Маяковского, д. 4',
                           'bank_account_number': '987654321098'
                       }
                   ])
    
    # Заполнение таблицы measurement_units
    op.bulk_insert(t_mu,
                   [
                       {
                           'id': 1,
                           'unit': 'Килограммы'
                       },
                       {
                           'id': 2,
                           'unit': 'Метры'
                       },
                       {
                           'id': 3,
                           'unit': 'Литры'
                       }
                   ])
    
    # Заполнение таблицы materials
    op.bulk_insert(t_materials,
                   [
                       {
                           'id': 1,
                           'class_code': 'Класс 1',
                           'group_code': 'Группа 1',
                           'name': 'Цемент',
                           'measurement_unit_code': 1  # Килограммы
                       },
                       {
                           'id': 2,
                           'class_code': 'Класс 2',
                           'group_code': 'Группа 2',
                           'name': 'Песок',
                           'measurement_unit_code': 1  # Килограммы
                       },
                       {
                           'id': 3,
                           'class_code': 'Класс 3',
                           'group_code': 'Группа 3',
                           'name': 'Вода',
                           'measurement_unit_code': 3  # Литры
                       }
                   ])

    # Заполнение таблицы storage_units
    op.bulk_insert(t_su,
                   [
                       {
                           'id': 1,
                           'order_number': 1001,
                           'date': datetime.now(),
                           'supplier_code': 1,  # Поставщик 1
                           'balance_account': '123456',
                           'document_code': 'DOC001',
                           'document_number': 'DOCNUM001',
                           'material_code': 1,  # Цемент
                           'quantity_received': 100,
                           'unit_price': 50.0
                       },
                       {
                           'id': 2,
                           'order_number': 1002,
                           'date': datetime.now(),
                           'supplier_code': 2,  # Поставщик 2
                           'balance_account': '654321',
                           'document_code': 'DOC002',
                           'document_number': 'DOCNUM002',
                           'material_code': 2,  # Песок
                           'quantity_received': 200,
                           'unit_price': 30.0
                       },
                       {
                           'id': 3,
                           'order_number': 1003,
                           'date': datetime.now(),
                           'supplier_code': 1,  # Поставщик 1
                           'balance_account': '789012',
                           'document_code': 'DOC003',
                           'document_number': 'DOCNUM003',
                           'material_code': 3,  # Вода
                           'quantity_received': 150,
                           'unit_price': 10.0
                       }
                   ])

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('measurement_units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_measurement_units'))
    )
    op.create_table('suppliers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('inn', sa.String(length=12), nullable=False),
    sa.Column('legal_address', sa.String(length=100), nullable=False),
    sa.Column('bank_address', sa.String(length=100), nullable=False),
    sa.Column('bank_account_number', sa.String(length=12), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_suppliers'))
    )
    op.create_table('materials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_code', sa.String(), nullable=False),
    sa.Column('group_code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('measurement_unit_code', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['measurement_unit_code'], ['measurement_units.id'], name=op.f('fk_materials_measurement_unit_code_measurement_units')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_materials'))
    )
    op.create_table('storage_units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_number', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('supplier_code', sa.Integer(), nullable=False),
    sa.Column('balance_account', sa.String(length=12), nullable=False),
    sa.Column('document_code', sa.String(length=10), nullable=False),
    sa.Column('document_number', sa.String(length=10), nullable=False),
    sa.Column('material_code', sa.Integer(), nullable=False),
    sa.Column('quantity_received', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['material_code'], ['materials.id'], name=op.f('fk_storage_units_material_code_materials')),
    sa.ForeignKeyConstraint(['supplier_code'], ['suppliers.id'], name=op.f('fk_storage_units_supplier_code_suppliers')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_storage_units'))
    )
    data_upgrades()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('storage_units')
    op.drop_table('materials')
    op.drop_table('suppliers')
    op.drop_table('measurement_units')
    # ### end Alembic commands ###
