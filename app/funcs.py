from models import Material, Supplier
from sqlalchemy.orm import Session
from sqlalchemy import select

def suppier_count(material: Material):
    return len(material.suppliers)

def suppliers_by_bank(engine, bank_address: str):
    with Session(autoflush=False, bind=engine) as db:
        return list(db.execute(select(Supplier).filter_by(bank_address=bank_address)).scalars())

def material_suppliers(material: Material):
    return material.suppliers
