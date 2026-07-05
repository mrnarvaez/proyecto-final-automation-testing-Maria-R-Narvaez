import requests
import logging

class PostsPage:
    def __init__(self, base_url):
        self.base_url = f"{base_url}/posts"
        self.headers = {"Content-type": "application/json; charset=UTF-8"} # Centralizado
        logging.info(f"Inicializando PostsPage con URL base: {self.base_url}")

    def _log_response(self, response):
        """Método privado para evitar repetir logs de status code"""
        logging.info(f"Respuesta recibida con status code: {response.status_code}")

    def get_all_posts(self):
        logging.info("Enviando petición GET a /posts")
        response = requests.get(self.base_url)
        self._log_response(response)
        return response

    def create_post(self, title, body, user_id):
        payload = {"title": title, "body": body, "userId": user_id}
        logging.info(f"Enviando petición POST a /posts con el título: '{title}'")
        
        response = requests.post(self.base_url, json=payload, headers=self.headers)
        self._log_response(response)
        return response

    def delete_post(self, post_id):
        logging.info(f"Enviando petición DELETE para el post ID: {post_id}")
        response = requests.delete(f"{self.base_url}/{post_id}")
        self._log_response(response)
        return response