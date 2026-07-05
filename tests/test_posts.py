import pytest
from pages.posts_page import PostsPage

@pytest.fixture
def posts_page(base_url):
    return PostsPage(base_url)


def test_get_posts_validation(posts_page):
    """Caso 1: GET - Valida la obtención de posts y la estructura del JSON"""
    response = posts_page.get_all_posts()
    
    # Validaciones
    assert response.status_code == 200, f"Código de estado incorrecto: {response.status_code}"
    assert "application/json" in response.headers["Content-Type"], "El formato de respuesta no es JSON"
    
    json_data = response.json()
    assert isinstance(json_data, list), "La respuesta debería ser una lista de posts"
    assert len(json_data) > 0, "La lista de posts está vacía"
    
    # Validar la estructura del primer elemento
    first_post = json_data[0]
    assert "id" in first_post, "Falta el campo 'id' en el post"
    assert "title" in first_post, "Falta el campo 'title' en el post"
    assert "body" in first_post, "Falta el campo 'body' en el post"
    assert "userId" in first_post, "Falta el campo 'userId' en el post"


def test_create_post_validation(posts_page):
    """Caso 2: POST - Valida la creación de un nuevo recurso"""
    test_title = "Automatización con Pytest"
    test_body = "Curso de testing de APIs con Requests y Python"
    test_user_id = 1
    
    response = posts_page.create_post(title=test_title, body=test_body, user_id=test_user_id)
    
    # 201 = 'Created' (Creado con éxito)
    assert response.status_code == 201, f"Se esperaba 201 pero se obtuvo {response.status_code}"
    
    json_data = response.json()
    # Validamos que los datos enviados coincidan con la respuesta de la API
    assert json_data["title"] == test_title
    assert json_data["body"] == test_body
    assert json_data["userId"] == test_user_id
    assert "id" in json_data, "La API no retornó el ID del nuevo recurso"


def test_delete_post_validation(posts_page):
    """Caso 3: DELETE - Valida la eliminación de un recurso"""
    # Simulamos que eliminamos el post con ID 1
    post_id_to_delete = 1
    
    response = posts_page.delete_post(post_id_to_delete)
    
    # JSONPlaceholder retorna 200 OK.
    assert response.status_code == 200, f"Fallo al eliminar el post: {response.status_code}"
    
    # Validamos que la respuesta esté vacía.
    assert response.json() == {}, "El cuerpo de la respuesta debería estar vacío tras un DELETE"