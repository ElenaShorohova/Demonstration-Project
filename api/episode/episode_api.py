from api.api_request import APIClient


class EpisodeApi(APIClient):
    """Класс для работы с"""

    def __init__(self):
        super().__init__()
        self.url = f"{self.BASE_URL}/episode"

    def get_episodes(self):
        """Метод для получения всех эпизодов"""
        return self.request(method="GET", url=self.url)
