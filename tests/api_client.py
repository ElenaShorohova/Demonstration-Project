import logging
import requests
from requests.exceptions import RequestException, Timeout
from pydantic import BaseModel


class APIClient:
    """Базовый API-клиент для работы с Rick and Morty API"""

    BASE_URL = "https://rickandmortyapi.com/api"

    def __init__(self):
        self.session = requests.Session()

    def request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        response_model: type[BaseModel] | None = None,
        timeout: int = 5,
    ):
        """Отправляет запрос к API, логирует и валидирует ответ"""
        url = f"{self.BASE_URL}/{endpoint}"
        logging.info(f"Отправить {method} запрос на {url} с параметрами {params}")

        try:
            response = self.session.request(method, url, params=params, timeout=timeout)
            response.raise_for_status()  # Бросает исключение при 4xx/5xx

        except Timeout:
            logging.error(f"Таймаут запроса {method} {url}")
            return {"error": "Request timed out"}

        except requests.HTTPError:
            logging.error(f"Ошибка HTTP {response.status_code}: {response.text}")
            return {"error": f"HTTP error {response.status_code}"}

        except RequestException as e:
            logging.error(f"Ошибка сети: {str(e)}")
            return {"error": "Network error"}

        logging.info(f"Ответ ({response.status_code}): {response.text[:500]}")

        if response_model:
            return response_model.model_validate(
                response.json()
            )  # Валидация через Pydantic

        return response.json()


class RickAndMortyAPI(APIClient):
    """Клиент для работы с Rick and Morty API"""

    def get_character(self, character_id: int):
        """Получить персонажа по ID"""
        return self.request("GET", f"character/{character_id}")

    def get_all_characters(self, page: int = 1):
        """Получить список всех персонажей"""
        return self.request("GET", "character", params={"page": page})

    def get_episode(self, episode_id: int):
        """Получить эпизод по ID"""
        return self.request("GET", f"episode/{episode_id}")
