import pytest

from tests.api_client import RickAndMortyAPI
from tests.models import Character, Episode


@pytest.fixture(scope="module")
def api():
    return RickAndMortyAPI()


def test_get_character(api):
    """Проверяем, что можно получить персонажа Рика Санчеза"""
    character = api.get_character(1)
    validated_character = Character.model_validate(character)

    assert validated_character.id == 1
    assert validated_character.name == "Rick Sanchez"
    assert validated_character.species == "Human"


def test_get_all_characters(api):
    """Проверяем, что список персонажей загружается"""
    data = api.get_all_characters()

    assert "results" in data
    assert len(data["results"]) > 0


def test_get_episode(api):
    """Проверяем, что можно получить эпизод"""
    episode = api.get_episode(1)
    validated_episode = Episode.model_validate(episode)

    assert validated_episode.id == 1
    assert validated_episode.name == "Pilot"
    assert "characters" in validated_episode.characters
