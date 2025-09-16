# Gym Diary 🏋️‍♂️

Веб-приложение на [Django](https://www.djangoproject.com/), позволяющее вести дневник тренировок, отслеживать прогресс и
управлять планами занятий.

---

## 🚀 Установка и запуск

### Создание и активация виртуального окружения

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Настройка `pre-commit`

```bash
pre-commit install
chmod +x docker-push.sh
chmod +x bump-version.sh
```

### Настройка базы данных

```bash
python manage.py migrate
```

### Запуск сервера разработки

```bash
python manage.py runserver
```