from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.item import ItemCreate, ItemUpdate, ItemRead
from app.services.inventory_service import InventoryService
from typing import List

router = APIRouter(prefix="/api/items", tags=["items"])

@router.get("/", response_model=List[ItemRead])
def list_items(db: Session = Depends(get_db)):
    return InventoryService(db).get_all_items()

@router.get("/{item_id}", response_model=ItemRead)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return InventoryService(db).get_item(item_id)

@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return InventoryService(db).create_item(item)

@router.put("/{item_id}", response_model=ItemRead)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    return InventoryService(db).update_item(item_id, item)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    InventoryService(db).delete_item(item_id)
