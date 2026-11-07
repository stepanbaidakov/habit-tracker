# Habit Tracker

## Description

A Django REST API for tracking good habits, inspired by James Clear's book *Atomic Habits*.

The application allows users to create and manage personal habits, share public habits, and receive Telegram reminders about scheduled activities.

## Features

- **User authentication** — registration and authorization.
- **Habit management** — create, view, update, and delete personal habits.
- **Public habits** — browse publicly available habits created by other users.
- **Habit rewards** — associate a pleasant habit or a separate reward with a useful habit..
- **Telegram integration** — receive reminders about scheduled habits.

## Habit Model

Each habit contains information describing the action, when it should be performed, and where it should take place.

The main habit attributes include:

- **User** — the user who created the habit.
- **Place** — where the habit should be performed.
- **Time** — when the habit should be performed.
- **Action** — the activity associated with the habit.
- **Pleasant habit flag** — indicates whether the habit is a pleasant habit.
- **Related habit** — a pleasant habit associated with a useful habit.
- **Frequency** — how often the habit should be performed, in days. The default is daily.
- **Reward** — a reward received after completing the habit.
- **Execution time** — the estimated time required to perform the habit.
- **Public status** — determines whether other users can view the habit.

## Habit Validation Rules

The application enforces the following business rules:

- A habit cannot have both a related pleasant habit and a separate reward.
- Habit execution time cannot exceed 120 seconds.
- A related habit must be marked as pleasant.
- A pleasant habit cannot have its own reward or related habit.
- A habit must be performed at least once every seven days.

## Access Control

- Users can create, view, update, and delete their own habits.
- Users can view public habits created by other users.
- Public habits cannot be edited or deleted by other users.

## Local Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/stepanbaidakov/habit-tracker.git
```

### 2. Navigate to the project directory

```bash
cd habit-tracker
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Linux/macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file based on the `.env.sample` template:

```bash
cp .env.sample .env
```

On Windows, copy the template manually if the `cp` command is unavailable.

Configure the required environment variables, including the Django secret key, database connection, Telegram bot token, and any other settings required by the application.

### 7. Apply database migrations

```bash
python manage.py migrate
```

### 8. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Running with Docker

### 1. Configure environment variables

Create a `.env` file based on `.env.sample` and fill in the required settings.

### 2. Build and start the application

```bash
docker compose up -d --build
```

### 3. Apply database migrations

```bash
docker compose exec web python manage.py migrate
```

### 4. Check the running containers

```bash
docker compose ps
```

View application logs if necessary:

```bash
docker compose logs -f
```

### 5. Stop the application

```bash
docker compose down
```

## Usage

### User Registration and Authentication

Register a user and authenticate using the API endpoints provided by the application.

Authenticated users can manage their own habits according to the configured permissions.

### Managing Habits

Users can create habits by specifying the action, place, scheduled time, frequency, and optional reward information.

A useful habit can have either a separate reward or a related pleasant habit, but not both.

### Public Habits

Users can browse public habits shared by other users and use them as inspiration for building their own routines.

### Telegram Reminders

Activate the Telegram bot to receive habit reminders:

[https://t.me/HaibitGoodBot](https://t.me/HaibitGoodBot)

Reminders depend on the Telegram integration and scheduled task configuration.

## API Documentation

API documentation is available through Swagger UI and ReDoc, provided these endpoints are enabled in the deployed application.

- **Swagger UI:** `.../swagger/`
- **ReDoc:** `.../redoc/`

These URLs refer to the configured deployment address. Replace them if the application is hosted elsewhere.

## CI/CD

The deployment workflow is located at:

```text
.github/workflows/cd.yml
```

To configure GitHub Actions secrets, navigate to:

**Settings → Secrets and variables → Actions**

Add the following secrets if they are referenced by the workflow:

```text
DOCKER_HUB_ACCESS_TOKEN
DOCKER_HUB_USERNAME
SECRET_KEY
SERVER_IP
SSH_KEY
SSH_USER
```

When changes are pushed to the configured main branch, the workflow may perform the following steps, depending on its implementation:

1. Retrieve the latest source code.
2. Install dependencies.
3. Run automated tests.
4. Build Docker images.
5. Connect to the server via SSH.
6. Update the application.
7. Restart Docker containers.

## Deployment

The deployment server must have the following software installed:

- Docker
- Docker Compose

Verify the installation:

```bash
docker --version
docker compose version
```

### 1. Copy the Docker Compose file to the server

Copy `docker-compose.yml` from the local project to the deployment server. The application source code does not need to be copied because the server uses pre-built Docker images.

### 2. Configure environment variables

Create the `.env` file based on `.env.sample`:

```bash
cp .env.sample .env
```

Edit `.env` and configure the required production environment variables:

```bash
nano .env
```

### 4. Check the running containers

```bash
docker compose ps
```

View application logs if necessary:

```bash
docker compose logs -f
```

## Technologies

- Python
- Django
- Django REST Framework
- PostgreSQL or another configured database
- Telegram Bot API
- Celery
- Docker and Docker Compose
- GitHub Actions for CI/CD
