import logging
import os

# Создаем папку logs, если её нет
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Настраиваем логгер
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler("logs/api_test.log", mode="w"),
        logging.StreamHandler(),
    ],
)

api_logger = logging.getLogger("api_logger")
