from pydantic import BaseModel


class Character(BaseModel):
    """Модель персонажа"""
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: dict
    location: dict
    image: str
    episode: list[str]
    url: str
    created: str


class Episode(BaseModel):
    """Модель эпизода"""
    id: int
    name: str
    air_date: str
    episode: str
    characters: list[str]
    url: str
    created: str
