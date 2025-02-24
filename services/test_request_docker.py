import requests

# Определяем item_id и параметры модели
user_id = "123"
model_params = {
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

# вывод входных данных
print ('Параметры модели: ', model_params)

# Отправляем post запрос
response = requests.post("http://localhost:8081/api/flats/", json=model_params)