# Трекер полезных привычек

## Описание:

API-сервер для трекинга полезных привычек

## Локальная установка и запуск приложения

* Клонируйте репозиторий:
  ```git clone https://github.com/stepanbaidakov/habit-tracker.git```
* Перейдите в директорию проекта ```cd habit-tracker```
* Создайте виртуальное окружение ```python -m venv venv```
* Активируйте его 

**Linux/macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```
* Установите необходимые библиотеки:

```bash
pip install -r requirements.txt
```

* Настройка файла ```.env``` оп шаблону ```.env.samle```
* Выполните миграции:

```bash
python manage.py migrate
```
* Запустите сервер разработки:

```bash
python manage.py runserver
```
## Запуск через Docker
* Создайте файл `.env`оп шаблону ```.env.samle```
* Запуск приложения
```bash
docker compose up --build
```
* Запуск в фоновом режиме

```bash
docker compose up -d
```
* Применение миграций:

```bash
docker compose exec web python manage.py migrate
```
## CI/CD
* Workflow расположен:

```
.github/workflows/cd.yml
```
* Для работы CI/CD необходимо добавить секреты:
```
Settings → Secrets and variables → Actions
```

```
SERVER_HOST
SERVER_USER
SERVER_SSH_KEY
```
## Деплой на сервер 
* На сервере должны быть установлены:

- Git
- Docker
- Docker Compose
* Проверка установки:

```bash
git --version
docker --version
docker compose version
```
* Создайте файл `.env`:

```bash
nano .env
```
При отправке изменений в основную ветку выполняются следующие этапы:

1. Получение актуального кода из репозитория.
2. Установка зависимостей.
3. Запуск автоматических тестов.
4. Сборка Docker-образов.
5. Подключение к серверу по SSH.
6. Обновление приложения.
7. Перезапуск Docker-контейнеров

## Использование

* Возможность регистрации и дальнейшей авторизации для создания полезных привычек через API запросы по IP-адресу
  111.88.157.137
* У полезных привычек может быть указаны либо приятные привычки в качестве вознаграждения, либо свое
  вознаграждение на прямую
* Переход и активация бота https://t.me/HaibitGoodBot для получения напоминаний по привычкам

## Документация

Для получения дополнительной информации обратитесь к документации в swagger http://111.88.157.137:81/swagger/ или
http://111.88.157.137:81/redoc/

## Лицензия