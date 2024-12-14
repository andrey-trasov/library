from sqlalchemy.orm import Session

from models.borrow_models import Borrow
from schemas.borrow_schema import BorrowCreate, BorrowUpdate


# Создание записи о выдаче книги
async def create_borrow(db: Session, borrow: BorrowCreate):
    db_borrow = Borrow(**borrow.dict())
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow

# Получение информации о выдаче по id
async def read_borrow(db: Session, id: int):
    return db.query(Borrow).filter(Borrow.id == id).first()

# Получение списка всех выдач
async def read_borrows(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Borrow).offset(skip).limit(limit).all()

# Завершение выдачи
async def update_borrows(db: Session, id: int, author: BorrowUpdate):
    db_borrow = db.query(Borrow).filter(Borrow.id == id).first()
    for var, value in vars(author).items():
        setattr(db_borrow, var, value) if value else None
    db.commit()
    db.refresh(db_borrow)
    return db_borrow
