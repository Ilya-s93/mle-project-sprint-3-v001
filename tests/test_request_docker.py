import requests
import os
import json
from dotenv import load_dotenv

load_dotenv('../services/.env')

# Определяем user_id и параметры модели
user_id = os.getenv('user_id')
model_params = json.loads(os.getenv('model_params'))

# вывод входных данных
print ('Параметры модели: ', model_params)

url = f"http://localhost:8081/api/get_prediction/?user_id={user_id}"

# Отправляем post запрос
response = requests.post(url, json=model_params)