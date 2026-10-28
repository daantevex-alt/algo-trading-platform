# Algo Trading Platform

REST API backend для управления алгоритмическими торговыми стратегиями.

## Технологии

| Слой | Инструмент |
|------|-----------|
| Web-фреймворк | FastAPI |
| ORM | SQLAlchemy 2.x (async) |
| База данных | PostgreSQL (asyncpg) |
| Кэш | Redis |
| Валидация | Pydantic v2 |
| Безопасность | bcrypt |
| Python | 3.12+ |

## Архитектура

```
app/
├── main.py              # Точка входа, FastAPI-приложение
├── dependencies.py      # Фабрики зависимостей для Depends()
├── api/                 # Роутеры (HTTP-слой)
│   ├── users.py
│   └── strategies.py
├── services/            # Бизнес-логика
│   ├── User_service.py
│   └── strategy_service.py
├── repositories/        # Работа с БД (паттерн Repository)
│   ├── user_repositories.py
│   └── StrategyRepositories.py
├── db/
│   ├── session.py       # Создание движка и сессии SQLAlchemy
│   └── unit_of_work.py  # Паттерн Unit of Work (управление транзакцией)
├── models/              # SQLAlchemy-модели (таблицы)
│   └── model.py
├── schemas/             # Pydantic-схемы (входящие/исходящие данные)
│   ├── user.py
│   └── strategy.py
├── core/
│   ├── config.py        # Настройки через .env
│   ├── redis.py         # Клиент Redis
│   └── security.py      # Хэширование паролей
└── exceptions/          # Кастомные исключения + HTTP-обработчики
    └── user.py
```

## Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone https://github.com/YOUR_USERNAME/algo-trading-platform.git
cd algo-trading-platform
```

### 2. Создать виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Настроить окружение

```bash
cp .env.example .env
# Заполнить .env реальными данными PostgreSQL и Redis
```

### 5. Запустить приложение

```bash
uvicorn app.main:app --reload
```

API будет доступно по адресу: http://localhost:8000

Документация (Swagger UI): http://localhost:8000/docs

## API Endpoints

| Метод | Путь | Описание |
|-------|------|----------|
| `POST` | `/users/register` | Регистрация пользователя |
| `POST` | `/users/login` | Авторизация |
| `GET` | `/strategies/{id}` | Получить стратегию (с кэшем Redis) |
| `GET` | `/health` | Проверка работоспособности |

## Тесты

```bash
pytest tests/ -v
```

## Паттерны в проекте

- **Repository** — репозитории изолируют запросы к БД от бизнес-логики
- **Unit of Work** — гарантирует атомарность операций (всё или ничего)
- **Dependency Injection** — все зависимости передаются через `Depends()`
- **Redis cache** — стратегии кэшируются на 60 секунд для снижения нагрузки на БД
- **SKIP LOCKED** — пример реализации очереди задач на PostgreSQL без внешних очередей (см. `app/pracrike/lockeds.py`)
