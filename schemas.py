from pydantic import BaseModel, HttpUrl
from typing import Optional
from enum import Enum

class CategoryEnum(str, Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UnitEnum(str, Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    psck = "psck"

class ProductBase(BaseModel):
    name: str
    category: CategoryEnum
    description: Optional[str]
    product_image: Optional[HttpUrl]
    sku: str
    unit_of_measure: UnitEnum
    lead_time: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    product_id: int
    created_date: Optional[str]
    updated_date: Optional[str]

    class Config:
        orm_mode = True
