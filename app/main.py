from sqlalchemy import create_engine, select
from models import Material
from funcs import *
from config import SQLALCHEMY_DATABASE_URI
import json

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

if __name__ == "__main__":
    with Session(autoflush=False, bind=engine) as db:
        material = db.execute(select(Material).filter_by(id=1)).scalar()
        print(suppier_count(material))
        suppliers = suppliers_by_bank(engine, 'Санкт-Петербург, ул. Маяковского, д. 4')
        print(json.dumps(suppliers[0]))
        # for supplier in suppliers:
        #     print(f'\{'', '{supplier.name}', \}')
        #     pass
    pass
