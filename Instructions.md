# Инструкции по запуску микросервиса

Каждая инструкция выполняется из директории репозитория mle-sprint3-completed
Если необходимо перейти в поддиректорию, напишите соотвесвтующую команду

## 1. FastAPI микросервис в виртуальном окружение
```python
# команды создания виртуального окружения
# и установки необходимых библиотек в него
# клонирование репозитория
git clone https://github.com/yandex-praktikum/mle-project-sprint-3-v001
# переход в директорию
cd mle-project-sprint-3-v001/services
# создание виртуального пространства
python3.10 -m venv .venv_project_sprint-3
# запуск виртуального пространства
source .venv_project_sprint-3/bin/activate
# установка необходимых библиотек
pip install -r requirements.txt

# команда запуска сервиса с помощью uvicorn
uvicorn flats_app:app --reload --port 8081 --host 0.0.0.0

### Пример curl-запроса к микросервису
bash
```
curl -X 'POST' \
  'http://127.0.0.1:8081/api/flats/?user_id=123' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "build_year": 2014,
  "building_type_int": 2,
  "latitude": 55.596458,
  "longitude": 37.599823,
  "ceiling_height": 2.8,
  "flats_count": 912,
  "floors_total": 23,
  "has_elevator": false,
  "floor": 10,
  "is_apartment": false,
  "kitchen_area": 11.6,
  "living_area": 17.1,
  "rooms": 1,
  "studio": false,
  "total_area": 42
}'
```


## 2. FastAPI микросервис в Docker-контейнере

```bash
# Строим образ
docker image build . --tag ml_image -f Dockerfile_ml_service

# команда для запуска микросервиса
docker container run --publish 8081:8081 --env-file .env --name ml_container ml_image

# запуск теста
python test_request_docker.py

# остановить контейнер
docker stop ml_container

# удалить контейнер
docker rm ml_container
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://127.0.0.1:8081/api/flats/?user_id=123' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "build_year": 2014,
  "building_type_int": 2,
  "latitude": 55.596458,
  "longitude": 37.599823,
  "ceiling_height": 2.8,
  "flats_count": 912,
  "floors_total": 23,
  "has_elevator": false,
  "floor": 10,
  "is_apartment": false,
  "kitchen_area": 11.6,
  "living_area": 17.1,
  "rooms": 1,
  "studio": false,
  "total_area": 42 
  }'
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию
cd mle-project-sprint-3-v001/services

# команда для запуска микросервиса в режиме docker compose
docker compose up --build

# команда запуска теста
python test_request_docker.py

# команда остановки микросервиса
docker compose down

# команда проверки действующих микросервисов
docker compose ls
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://127.0.0.1:8081/api/flats/?user_id=123' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "build_year": 2014,
  "building_type_int": 2,
  "latitude": 55.596458,
  "longitude": 37.599823,
  "ceiling_height": 2.8,
  "flats_count": 912,
  "floors_total": 23,
  "has_elevator": false,
  "floor": 10,
  "is_apartment": false,
  "kitchen_area": 11.6,
  "living_area": 17.1,
  "rooms": 1,
  "studio": false,
  "total_area": 42 
  }'
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует <10> запросов в течение <30> секунд.

```
# команды необходимые для запуска скрипта
python test_requests10-grafana.py
```

Адреса сервисов:
- микросервис: http://localhost:8081
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000