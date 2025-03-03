import pytest
import allure
from tests.api_client import RickAndMortyAPI


@pytest.fixture(scope="module")
def api():
    return RickAndMortyAPI()


@allure.feature("Characters API")
@allure.story("Получение персонажа по ID")
@allure.step("Проверяем, что персонаж 1 - это Рик Санчез")
def test_get_character(api):
    response = api.get_character(1)
    with allure.step("Проверяем статус код"):
        assert response["id"] == 1
    with allure.step("Проверяем имя персонажа"):
        assert response["name"] == "Rick Sanchez"
    with allure.step("Проверяем расу персонажа"):
        assert response["species"] == "Human"


@allure.feature("Episodes API")
@allure.story("Получение эпизода по ID")
@allure.step("Проверяем, что первый эпизод называется 'Pilot'")
def test_get_episode(api):
    response = api.get_episode(1)
    with allure.step("Проверяем статус код"):
        assert response["id"] == 1
    with allure.step("Проверяем название эпизода"):
        assert response["name"] == "Pilot"