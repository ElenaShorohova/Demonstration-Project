"""Конфигурация с параметрами запуска"""

from pathlib import Path

from selenium.webdriver.chrome.webdriver import WebDriver


class Config:
    """Абстрактный класс с параметрами запуска. Заполняется при старте проекта"""

    driver: WebDriver
    browser: str
    is_remote: bool = False
    is_headless: bool = False
    stand: str
    web_url: str
    log_level = "INFO"
    test_data_dir = Path("test_data").absolute()
    timeout = 30
