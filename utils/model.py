"""Методы валидации ответа по схеме Pydantic"""

from json import dumps
from typing import Type

from allure import attach, step
from pydantic import BaseModel, ValidationError
from pytest import fail

from utils import logger


@step("Валидация тела ответа по схеме")
def is_valid(model: Type[BaseModel], response: dict):
    """Валидировать тело ответа по схеме

    Args:
        model: класс модели Pydantic
        response: тело ответа
    """
    with step("Проверить тело ответа схеме"):
        _model, _response = model.model_json_schema(), dumps(response)
        attach(_response, "Тело ответа")
        attach(str(_model), "Модель")

        try:
            model.model_validate(response)

        except ValidationError as e:
            logger.error(
                "Ошибка валидации тела ответа"
                f"Ошибка {e}, Модель: {_model}, Тело ответа: {_response}"
            )
            fail(reason=str(e))


def convert_model(
    model: BaseModel, is_json: bool = False, **kwargs
) -> list | dict | str:
    """Преобразование модели в объект для отправки в request: str, dict, list

    Args:
        model: объект модели;
        is_json:    True - результат возвращается в формате json;
                    False - результат возвращается в dict/list
        **kwargs: аргументы для метода преобразования
    """
    result = model.model_dump_json(**kwargs) if is_json else model.model_dump(**kwargs)

    if "__root__" in result:
        result = result["__root__"]

    is_list = True if isinstance(result, list) else False

    logger.debug(
        "Преобразование модели"
        f"Модель: {model}, "
        f'Преобразование: {"json" if is_json else "list" if is_list else "dict"}'
        f"Результат: {result}"
    )

    return result
