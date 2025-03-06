from enum import StrEnum
from typing import Any, Type

from pydantic import BaseModel
from requests import request, Request as src_Request

from api.api_response import CustomResponse
from utils.logger import log_request, log_response
from utils.model import convert_model


class MethodEnum(StrEnum):
    """Перечисление доступных методов запроса"""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class APIClient:
    """Базовый API-клиент для работы с Rick and Morty API"""

    BASE_URL = "https://rickandmortyapi.com/api"

    headers, params, data, files, json = {}, {}, {}, {}, {}

    def request(
        self,
        url: str,
        method: str,
        headers: dict[str, Any] | None = None,
        data: dict | list | str | bytes | BaseModel | None = None,
        params: dict[str, Any] | None = None,
        json: dict | list | BaseModel | None = None,
        response_model: Type[BaseModel] | None = None,
        response_error_model: Type[BaseModel] | None = None,
        timeout: int = 5,
        **kwargs,
    ) -> CustomResponse:
        """Метод для отправки запроса.
         Получает ответ и валидирует запрос и ответ

        Args:
            url: адрес
            method: HTTP-метод
            headers: заголовки запроса
            data: тело запроса
            params: параметры запроса
            json: тело запроса в формате JSON
            response_model: модель для валидации ответа
            response_error_model: модель для валидации ошибок
            timeout: таймаут перед отправкой запроса
            kwargs: аргументы для преобразования объекта модели

        Returns:
            объект CustomResponse
        """
        if isinstance(data := data if data else self.data, BaseModel):
            data = convert_model(model=data, is_json=True, **kwargs)

        if isinstance(json := json if json else self.json, BaseModel):
            json = convert_model(model=json, **kwargs)

        log_request(
            request=src_Request(
                url=url,
                method=f"{method}",
                headers=headers if headers else self.headers,
                data=data if data else self.data,
                params=params if params else self.params,
                json=json if json else self.json,
            ).prepare()
        )

        response = request(
            url=url,
            method=f"{method}",
            headers=headers if headers else self.headers,
            params=params if params else self.params,
            data=data if data else self.data,
            json=json if json else self.json,
            verify=False,
            timeout=timeout,
        )
        log_response(response=response)

        return CustomResponse(
            response=response,
            response_model=response_model,
            response_error_model=response_error_model,
        )
