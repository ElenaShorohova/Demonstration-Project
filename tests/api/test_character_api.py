import allure
from pytest import mark

from api.character.character_api import CharacterApi


@mark.api
@allure.feature("Characters API")
@allure.story("Получение персонажа по ID")
@allure.step("Проверить, что персонаж 1 - это Рик Санчез")
def test_get_character():
    response = CharacterApi().get_character()
    response = response.json()
    with allure.step("Проверить id персонажа"):
        assert response["results"][0]["id"] == 1
    with allure.step("Проверить имя персонажа"):
        assert response["results"][0]["name"] == "Rick Sanchez"
    with allure.step("Проверить расу персонажа"):
        assert response["results"][0]["species"] == "Human"
