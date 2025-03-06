import allure

from api.episode.episode_api import EpisodeApi


@allure.feature("Episodes API")
@allure.story("Получение эпизода по ID")
@allure.step("Проверить, что первый эпизод называется 'Pilot'")
def test_get_episode():
    response = EpisodeApi().get_episodes()
    response = response.json()
    with allure.step("Проверить id первого эпизода"):
        assert response["results"][0]["id"] == 1
    with allure.step("Проверить название эпизода"):
        assert response["results"][0]["name"] == "Pilot"
