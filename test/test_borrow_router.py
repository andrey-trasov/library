from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_post_create_borrow():
    """Создание записи о выдаче книги"""
    borrows_data = {
        "book_id": 2,
        "readers_name": "Test",
        "issue_date": "2024-12-17"
}

    response = client.post("/borrows", json=borrows_data)
    assert response.status_code == 200

def test_get_read_borrows():
    """Получение списка всех выдач"""
    response = client.get("/borrows")
    assert response.status_code == 200

def test_get_read_borrow():
    """Получение информации о выдаче по id"""
    response = client.get("/borrows/1")
    assert response.status_code == 200

def test_patch_update_borrows():
    """Завершение выдачи"""
    borrows_data = {
        "return_date": "2024-12-17"
    }

    response = client.patch("/borrows/1/return", json=borrows_data)
    assert response.status_code == 200
