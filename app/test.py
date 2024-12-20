import pytest
from models import Material
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from funcs import suppier_count

test_data = {
    'count': [
        ('sqlite:///project.db', 1)
    ]
}


@pytest.mark.parametrize("database_uri, expected", test_data['count'])
def test_count(database_uri, expected):
    engine = create_engine(database_uri, echo=True)
    with Session(autoflush=False, bind=engine) as db:
        material = db.execute(select(Material).filter_by(id=1)).scalar()
        assert suppier_count(material) == expected
