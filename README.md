# API UI Pytest Demo

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ElenaShorohova/api_ui_pytest_demo/api-tests.yml?branch=main)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Pytest](https://img.shields.io/badge/pytest-passing-green)

## О проекте

Привет!
Меня зовут **Елена**, я **автотестер и разработчик этого проекта**.  
Этот репозиторий содержит **автоматизированные тесты API и UI** с использованием **pytest, Selenium и Allure**.

**Тестируемое API**: [Rick and Morty API](https://rickandmortyapi.com/)  
**UI-тесты**: Selenium
**Автоматизация CI/CD**: GitHub Actions + Docker  
**Уведомления**: Telegram-бот  

## 📂 Структура проекта

api_ui_pytest_demo/  
│── api/                     # API-клиент  
│── ui/                      # web pages  
│── tests/                   # Тесты  
│   ├── api/                 # Тесты API  
│   ├── ui/                  # Тесты UI  
│── utils/                   # Вспомогательные утилиты  
│── config.py                # Конфигурации  
│── conftest.py              # Фикстуры Pytest  
│── requirements.txt         # Зависимости  
│── pyproject.toml           # Poetry-конфигурация  
│── README.md                # Документация  

## Установка

Убедитесь, что у вас установлен **Python 3.12** и **Poetry**.  
1) Клонируйте репозиторий:
https://github.com/ElenaShorohova/Demonstration-Project.git

2) Установите зависимости:
poetry install

3) Активируйте виртуальное окружение:
poetry shell или poetry env use python3.12

Технологии

🔹 Язык: Python 3.12  
🔹 Фреймворк тестирования: Pytest  
🔹 API-тестирование: Requests, Pydantic  
🔹 UI-тестирование: Selenium  
🔹 Отчёты: Allure  
🔹 CI/CD: GitHub Actions, Docker  
🔹 Линтеры: Black, Flake8  
🔹 Уведомления: Telegram  
