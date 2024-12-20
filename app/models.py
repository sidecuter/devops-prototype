from datetime import datetime
from typing import Optional, List
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, Text, Integer, MetaData, Table, Column, Float

class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    })


db = SQLAlchemy(model_class=Base)

class StorageUnit(Base):
    __tablename__ = 'storage_units'

    id: Mapped[int] = mapped_column(primary_key=True)
    order_number: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    supplier_code: Mapped[int] = mapped_column(ForeignKey('suppliers.id'))
    balance_account: Mapped[int] = mapped_column(String(12), nullable=False)
    document_code: Mapped[str] = mapped_column(String(10), nullable=False)
    document_number: Mapped[str] = mapped_column(String(10), nullable=False)
    material_code: Mapped[int] = mapped_column(ForeignKey('materials.id'))
    quantity_received = Column(Integer, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)

    material: Mapped["Material"] = relationship('Material')
    supplier: Mapped["Supplier"] = relationship('Supplier')

    @property
    def measurement_unit_code(self):
        return self.material.measurement_unit_code

    @property
    def measurement_unit(self):
        return self.material.measurement_unit


class Material(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True)
    class_code = Column(String, nullable=False)
    group_code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    measurement_unit_code: Mapped[int] = mapped_column(ForeignKey('measurement_units.id'))

    measurement_unit: Mapped["MeasurementUnit"] = relationship('MeasurementUnit')
    storage_units: Mapped[List["StorageUnit"]] = relationship(back_populates='material', cascade='all, delete-orphan')

    @property
    def suppliers(self):
        return list(map(lambda su: su.supplier, self.storage_units))
    

class MeasurementUnit(Base):
    __tablename__ = 'measurement_units'

    id = Column(Integer, primary_key=True)
    unit = Column(String, nullable=False)


class Supplier(Base):
    __tablename__ = 'suppliers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    inn: Mapped[str] = mapped_column(String(12), nullable=False)
    legal_address: Mapped[str] = mapped_column(String(100), nullable=False)
    bank_address: Mapped[str] = mapped_column(String(100), nullable=False)
    bank_account_number: Mapped[str] = mapped_column(String(12), nullable=False)

    storage_units: Mapped[List["StorageUnit"]] = relationship(back_populates='supplier', cascade='all, delete-orphan')
    
    @property
    def materials(self):
        return list(map(lambda su: su.material, self.storage_units))
    
    def __eq__(self, value):
        return self.id == value.id


# Создание базы данных
# engine = create_engine('sqlite:///warehouse.db')  # Пример для SQLite
# Base.metadata.create_all(engine)