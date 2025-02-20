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
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:...' \
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose

```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует <...> запросов в течение <...> секунд ...

```
# команды необходимые для запуска скрипта
...
```

Адреса сервисов:
- микросервис: http://localhost:<port>
- Prometheus: ...
- Grafana: ...