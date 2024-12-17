
from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# class Database:
#     def get_user(self, user_id: int):
#         return {
#             "first_name": "Test first_name",
#             "last_name": "Test last_name",
#             "date_of_birth": "2024-12-16T16:04:28.032000"
#         }
#
# def get_database():
#     return Database()
#
# def test_post_create_author():
#     mock_db = MagicMock()
#     mock_db.get_user.return_value = {}
#
#     # Override the get_database dependency with the mock object
#     app.dependency_overrides[get_database] = lambda: mock_db
#
#     author_data = {
#         "first_name": "Test first_name",
#         "last_name": "Test last_name",
#         "date_of_birth": "2024-12-16T16:04:28.032000"
#     }
#
#     response = client.post("/authors", json=author_data)
#     assert response.status_code == 200




def test_post_create_author():
    """Создание автора"""
    author_data = {
        "first_name": "Test first_name",
        "last_name": "Test last_name",
        "date_of_birth": "2024-12-16T16:04:28.032000"
    }

    response = client.post("/authors", json=author_data)
    assert response.status_code == 200

def test_post_create_author2():
    """Создание автора c id 2"""
    author_data = {
        "first_name": "Test first_name",
        "last_name": "Test last_name",
        "date_of_birth": "2024-12-16T16:04:28.032000"
    }

    response = client.post("/authors", json=author_data)
    assert response.status_code == 200
def test_get_read_authors():
    """Получение списка авторов"""
    response = client.get("/authors")
    assert response.status_code == 200

def test_get_read_author():
    """Получение информации об авторе по id"""
    response = client.get("/authors/1")
    assert response.status_code == 200

def test_put_update_author():
    """Обновление информации об авторе"""
    author_data = {
        "first_name": "Test",
        "last_name": "Test",
        "date_of_birth": "2024-12-16T16:04:28.032000"
    }

    response = client.put("/authors/1", json=author_data)
    assert response.status_code == 200

def test_delete_delete_author():
    """Удаление автора"""
    response = client.delete("/authors/1")
    assert response.status_code == 200
