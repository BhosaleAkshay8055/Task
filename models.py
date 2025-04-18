from sqlalchemy import Column, BigInteger, String, Enum, Integer, TIMESTAMP
from sqlalchemy.sql import func
from database import Base
import enum

class CategoryEnum(str, enum.Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UnitEnum(str, enum.Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    psck = "psck"

class Product(Base):
    __tablename__ = "products"

    product_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)
    description = Column(String(250))
    product_image = Column(String)  # URL
    sku = Column(String(100))
    unit_of_measure = Column(Enum(UnitEnum))
    lead_time = Column(Integer)  # in days
    created_date = Column(TIMESTAMP, server_default=func.now())
    updated_date = Column(TIMESTAMP, onupdate=func.now())
