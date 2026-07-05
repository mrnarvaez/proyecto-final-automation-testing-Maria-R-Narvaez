import pytest
from pages.posts_page import PostsPage

@pytest.fixture
def posts_page(base_url):
    return PostsPage(base_url)

@pytest.mark.smoke
def test_get_posts_validation(posts_page):
    """Caso 1: GET - Valida la obtención de posts y la estructura del JSON"""
    response = posts_page.get_all_posts()
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    
    json_data = response.json()
    assert isinstance(json_data, list) and len(json_data) > 0
    
    first_post = json_data[0]
    assert all(k in first_post for k in ("id", "title", "body", "userId"))

@pytest.mark.regression
def test_create_post_validation(posts_page):
    """Caso 2: POST - Valida la creación de un nuevo recurso"""
    test_title, test_body, test_user_id = "Automatización", "Curso de testing", 1
    response = posts_page.create_post(title=test_title, body=test_body, user_id=test_user_id)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["title"] == test_title and json_data["userId"] == test_user_id

@pytest.mark.regression
def test_delete_post_validation(posts_page):
    """Caso 3: DELETE - Valida la eliminación de un recurso"""
    response = posts_page.delete_post(1)
    assert response.status_code == 200
    assert response.json() == {}