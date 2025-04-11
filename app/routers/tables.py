from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Table
from app.schemas.schemas import TableCreate

router = APIRouter()

@router.get("/tables/")
def get_tables(db: Session = Depends(get_db)):
    return db.query(Table).all()

@router.post("/tables/")
def create_table(table: TableCreate, db: Session = Depends(get_db)):
    new_table = Table(**table.dict())
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table
