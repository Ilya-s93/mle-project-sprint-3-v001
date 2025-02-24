from fastapi import FastAPI, Body
from .fast_api_handler import FastApiHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram
from prometheus_client import Counter


# Создаем приложение Fast API
app = FastAPI()

# инициализируем и запускаем экпортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

main_app_predictions = Histogram(
    # имя метрики
    "main_app_predictions",
    #описание метрики
    "Histogram of predictions",
    #указаываем корзины для гистограммы
    buckets=(1, 2, 4, 5, 10)
)

main_app_counter_pos = Counter("main_app_counter_pos", "Count of positive predictions")

# обрабатываем запросы к корню приложения
@app.get("/")
def read_root():
    return {"Hello ML-engineer"}

# Создаем обработчик запросов для API
app.handler = FastApiHandler()


@app.post("/api/flats/") 
def get_prediction_for_item(
    user_id: str,
    model_params: dict = Body(
        example={
            'build_year': 2014,
            'building_type_int': 2,
            'latitude': 55.596458,
            'longitude': 37.599823,
            'ceiling_height': 2.8,
            'flats_count': 912,
            'floors_total': 23,
            'has_elevator': False,
            'floor': 10,
            'is_apartment': False,
            'kitchen_area': 11.6,
            'living_area': 17.1,
            'rooms': 1,
            'studio': False,
            'total_area': 42.0
        }
    )
):
    """Функция для получения стоимости квартиры.

    Args:
        user_id (str): Идентификатор пользователя.
        model_params (dict): Параметры пользователя, которые мы должны подать в модель.

    Returns:
        dict: Предсказание стоимости.
    """
    main_app_counter_pos.inc()
    all_params = {
        "user_id": user_id,
        "model_params": model_params
    }

    response = app.handler.handle(all_params)
    main_app_predictions.observe(response['prediction'])

    return response