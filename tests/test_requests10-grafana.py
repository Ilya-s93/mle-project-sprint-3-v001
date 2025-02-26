import requests
import time

def req_post(num, tm):
    for i in range(num):
        # Определяем user_id и параметры модели
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

        url = f"http://localhost:8081/api/get_prediction/?user_id={user_id}"

        # Отправляем post запрос
        response = requests.post(url, json=model_params)
        if i == num/2:
            time.sleep(tm)
        time.sleep(2)

req_post(10, 30)