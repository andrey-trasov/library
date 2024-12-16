from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from config.config_bd import SessionLocal
from schemas.borrow_schema import BorrowOut, BorrowCreate, BorrowUpdate
from services.borrow_service import create_borrow, read_borrows, read_borrow, update_borrows

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Создание записи о выдаче книги
@router.post("/borrows", response_model=BorrowOut)
async def post_create_borrow(borrow: BorrowCreate, db: Session = Depends(get_db)):
    """Создание записи о выдаче книги"""
    return await create_borrow(db, borrow)

# Получение списка всех выдач
@router.get("/borrows", response_model=List[BorrowOut])
async def get_read_borrows(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Получение списка всех выдач"""
    borrows = await read_borrows(db, skip, limit)
    return borrows

# Получение информации о выдаче по id
@router.get("/borrows/{id}", response_model=BorrowOut)
async def get_read_borrow(id: int, db: Session = Depends(get_db)):
    """Получение информации о выдаче по id"""
    db_book = await read_borrow(db, id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Завершение выдачи
@router.patch("/borrows/{id}/return", response_model=BorrowOut)
async def put_update_borrows(id: int, reader: BorrowUpdate, db: Session = Depends(get_db)):
    """Завершение выдачи"""
    return await update_borrows(db, id, reader)