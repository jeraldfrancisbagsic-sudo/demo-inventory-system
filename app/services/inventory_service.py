from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models import Item
from app.schemas.item import ItemCreate, ItemUpdate, ItemRead

class InventoryService:
    def __init__(self, db: Session):
        self.db = db

    def create_item(self, item: ItemCreate) -> ItemRead:
        db_item = Item(**item.model_dump())
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return ItemRead.model_validate(db_item)

    def get_item(self, item_id: int) -> ItemRead:
        db_item = self.db.query(Item).filter(Item.id == item_id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return ItemRead.model_validate(db_item)

    def get_all_items(self) -> list[ItemRead]:
        items = self.db.query(Item).all()
        return [ItemRead.model_validate(item) for item in items]

    def update_item(self, item_id: int, item: ItemUpdate) -> ItemRead:
        db_item = self.db.query(Item).filter(Item.id == item_id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        for field, value in item.model_dump(exclude_unset=True).items():
            setattr(db_item, field, value)
        self.db.commit()
        self.db.refresh(db_item)
        return ItemRead.model_validate(db_item)

    def delete_item(self, item_id: int) -> None:
        db_item = self.db.query(Item).filter(Item.id == item_id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        self.db.delete(db_item)
        self.db.commit()
