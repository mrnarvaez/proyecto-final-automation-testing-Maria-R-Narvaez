import pytest
from pages.users_page import UsersPage

@pytest.fixture
def users_page(base_url):
    return UsersPage(base_url)

@pytest.mark.smoke
def test_get_all_users_status_code(users_page):
    """Caso: Validar que el endpoint de usuarios responda 200"""
    response = users_page.get_all_users()
    assert response.status_code == 200

@pytest.mark.regression
def test_get_specific_user(users_page):
    """Caso: Validar la obtención de un usuario específico por ID"""
    user_id = 1
    response = users_page.get_user_by_id(user_id)
    assert response.status_code == 200
    assert response.json()["id"] == user_id