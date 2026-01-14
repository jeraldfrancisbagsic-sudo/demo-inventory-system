from pydantic import BaseModel, Field, ConfigDict, validator
from typing import Optional

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    price: float = Field(..., ge=0)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    quantity: Optional[int] = Field(None, ge=0)
    price: Optional[float] = Field(None, ge=0)

class ItemRead(ItemBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
