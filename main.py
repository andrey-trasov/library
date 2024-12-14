from fastapi import FastAPI
from config.config_bd import engine, Base, database, SessionLocal
from routers import author_router, book_router, borrow_router

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(author_router.router)
app.include_router(book_router.router)
app.include_router(borrow_router.router)


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


