import requests
import logging

class UsersPage:
    def __init__(self, base_url):
        self.base_url = f"{base_url}/users"
        logging.info(f"Inicializando UsersPage con URL base: {self.base_url}")

    def get_all_users(self):
        logging.info("Enviando petición GET a /users")
        response = requests.get(self.base_url)
        logging.info(f"Respuesta recibida con status: {response.status_code}")
        return response

    def get_user_by_id(self, user_id):
        logging.info(f"Consultando usuario con ID: {user_id}")
        response = requests.get(f"{self.base_url}/{user_id}")
        return response