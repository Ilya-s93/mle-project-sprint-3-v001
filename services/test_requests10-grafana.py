import requests
import time


for i in range(10):
    # Определяем item_id и параметры модели
    user_id = str(i)
    model_params = {
        'build_year': 2005 + i,
        'building_type_int': 2,
        'latitude': 55.596458,
        'longitude': 37.599823,
        'ceiling_height': 2.8,
        'flats_count': 912,
        'floors_total': 23,
        'has_elevator': False,
        'floor': 3 + i,
        'is_apartment': False,
        'kitchen_area': 11.6 + i,
        'living_area': 17.1 + i,
        'rooms': 1 + i,
        'studio': False,
        'total_area': 42.0 + i
    }

    url = f"http://localhost:8081/api/flats/?user_id={user_id}"

    # Отправляем post запрос
    response = requests.post(url, json=model_params)
    if i == 5:
        time.sleep(10)
    time.sleep(2)