import pytest
from requests import Timeout

from tests.api_client import RickAndMortyAPI


@pytest.fixture(scope="module")
def api():
    return RickAndMortyAPI()


def test_character_not_found(api):
    """Проверяем, что запрос персонажа с несуществующим ID возвращает 404"""
    response = api.get_character(999999)
    assert "error" in response, "Должна быть ошибка"
    assert response["error"] == "HTTP error 404", "Ожидался статус 404"


def test_api_timeout(api, monkeypatch):
    """Проверяем, что при таймауте возвращается соответствующая ошибка"""
    monkeypatch.setattr(api.session, "request", lambda *args, **kwargs: pytest.raises(Timeout))
    response = api.get_character(1)
    assert response["error"] == "Request timed out", "Ожидался таймаут"