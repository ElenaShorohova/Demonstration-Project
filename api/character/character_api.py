from api.api_request import APIClient


class CharacterApi(APIClient):
    """Класс для работы с"""

    def __init__(self):
        super().__init__()
        self.url = f"{self.BASE_URL}/character"

    def get_character(self):
        """Метод для получения всех персонажей"""
        return self.request(method="GET", url=self.url)
