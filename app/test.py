import pytest
from models import Material, Supplier
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from funcs import suppier_count, suppliers_by_bank

test_data = {
    'count': [
        ('sqlite:///project.db', 1)
    ],
    'supplier': [
        ('sqlite:///project.db', Supplier(id=2, bank_account_number='987654321098', bank_address='Санкт-Петербург, ул. Маяковского, д. 4', inn='987654321098', legal_address='Санкт-Петербург, ул. Невский, д. 3', name='ЗАО Стройматериалы'))
    ]
}


@pytest.mark.parametrize("database_uri, expected", test_data['count'])
def test_count(database_uri, expected):
    engine = create_engine(database_uri, echo=True)
    with Session(autoflush=False, bind=engine) as db:
        material = db.execute(select(Material).filter_by(id=1)).scalar()
        assert suppier_count(material) == expected

@pytest.mark.parametrize("database_uri, expected", test_data['supplier'])
def test_suppliers(database_uri, expected):
    engine = create_engine(database_uri, echo=True)
    suppliers = suppliers_by_bank(engine, 'Санкт-Петербург, ул. Маяковского, д. 4')
    assert suppliers[0] == expected
