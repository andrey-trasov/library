from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_post_create_book():
    """Добавление книги"""
    author_data = {
        "title": "test",
        "description": "test",
        "author_id": 2,
        "number_books": 1
    }

    response = client.post("/books", json=author_data)
    assert response.status_code == 200


def test_post_create_book_2():
    """Добавление книги c id 2"""
    book_data = {
        "title": "test",
        "description": "test",
        "author_id": 2,
        "number_books": 1
    }

    response = client.post("/books", json=book_data)
    assert response.status_code == 200

def test_get_read_books():
    """Получение списка книг"""
    response = client.get("/books")
    assert response.status_code == 200

def test_get_read_book():
    """Получение информации о книге по id"""
    response = client.get("/books/1")
    assert response.status_code == 200

def test_put_update_book():
    book_data = {
        "title": "test",
        "description": "tests",
        "author_id": 2,
        "number_books": 1
    }

    response = client.put("/books/1", json=book_data)
    assert response.status_code == 200

def test_delete_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
