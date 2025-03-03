# Используем Python 3.12
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo 'export PATH="/root/.local/bin:$PATH"' >> /root/.bashrc && \
    echo 'export PATH="/root/.local/bin:$PATH"' >> /etc/environment

# Загружаем переменные окружения, чтобы Poetry был доступен
ENV PATH="/root/.local/bin:$PATH"

# Проверяем, что Poetry установлен
RUN /root/.local/bin/poetry --version

# Копируем файлы проекта
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN /root/.local/bin/poetry install --no-interaction --no-ansi --no-root

# Копируем весь проект
COPY . .

# Запуск тестов по умолчанию
CMD ["/root/.local/bin/poetry", "run", "pytest", "--alluredir=allure-results"]