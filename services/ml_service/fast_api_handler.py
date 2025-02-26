"""Класс FastApiHandler, который обрабатывает запросы API."""

import pickle
import pandas as pd


class FastApiHandler:
    """Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):
        """Инициализация переменных класса."""

        # Типы параметров запроса для проверки
        self.param_types = {
            "user_id": str,
            "model_params": dict
        }

        self.model_path = "models/pipeline_model.pkl"
        self.load_pipeline_model(model_path=self.model_path)
        
        # Необходимые параметры для предсказаний модели оттока
        self.required_model_params = [
            'build_year', 'building_type_int', 'latitude', 'longitude',
            'ceiling_height', 'flats_count', 'floors_total', 'has_elevator',
            'floor', 'is_apartment', 'kitchen_area', 'living_area', 'rooms',
            'studio', 'total_area'
        ]

    def load_pipeline_model(self, model_path: str):
        """Загружаем обученную модель оттока.
        Args:
            model_path (str): Путь до модели.
        """
        try:
            with open(model_path, "rb") as f:
                self.pipeline = pickle.load(f)
        except Exception as e:
            print(f"Failed to load model: {e}")

    def flats_predict(self, model_params: dict) -> float:
        """Предсказываем стоимость квартиры.

        Args:
            model_params (dict): Параметры для модели.

        Returns:
            float - стоимость рубли
        """
        model_param_values = [model_params[param] for param in self.required_model_params]
        model_param_values_df = pd.DataFrame([model_param_values], columns=self.required_model_params)
        return self.pipeline.predict(model_param_values_df)[0]
        
    def check_required_query_params(self, query_params: dict) -> bool:
        """Проверяем параметры запроса на наличие обязательного набора параметров.
        
        Args:
            query_params (dict): Параметры запроса.
        
        Returns:
                bool: True - если есть нужные параметры, False - иначе
        """
        if "user_id" not in query_params or "model_params" not in query_params:
            print("В запросе нет либо user_id, либо model_params")
            return False
        
        if not isinstance(query_params["user_id"], self.param_types["user_id"]):
            print("Неправильный тип user_id")
            return False
                
        if not isinstance(query_params["model_params"], self.param_types["model_params"]):
            print("Неправильный тип model_params")
            return False
        return True
    
    def check_required_model_params(self, model_params: dict) -> bool:
        """Проверяем параметры пользователя на наличие обязательного набора.
    
        Args:
            model_params (dict): Параметры пользователя для предсказания.
    
        Returns:
            bool: True - если есть нужные параметры, False - иначе
        """
        if set(model_params.keys()) == set(self.required_model_params):
            return True
        return False
    
    def validate_params(self, params: dict) -> bool:
        """Разбираем запрос и проверяем его корректность.
    
        Args:
            params (dict): Словарь параметров запроса.
    
        Returns:
            - **dict**: Cловарь со всеми параметрами запроса.
        """
        if self.check_required_query_params(params):
            print("All query params exist")
        else:
            print("Not all query params exist")
            return False
        
        if self.check_required_model_params(params["model_params"]):
            print("All model params exist")
        else:
            print("Not all model params exist")
            return False
        return True
		
    def handle(self, params):
        """Функция для обработки запросов API параметров входящего запроса.
    
        Args:
            params (dict): Словарь параметров запроса.
    
        Returns:
            - **dict**: Словарь, содержащий результат выполнения запроса.
        """
        try:
            # Валидируем запрос к API
            if not self.validate_params(params):
                print("Error while handling request")
                response = {"Error": "Problem with parameters"}
            else:
                model_params = params["model_params"]
                user_id = params["user_id"]
                print(f"Predicting for user_id: {user_id} and model_params:\n{model_params}")
                # Получаем предсказания модели
                prediction = self.flats_predict(model_params)
                response = {
                    "user_id": user_id, 
                    "prediction": prediction
                }
        except Exception as e:
            print(f"Error while handling request: {e}")
            return {"Error": "Problem with request"}
        else:
            return response

if __name__ == "__main__":

    # Создаем тестовый запрос
    test_params = {
	    "user_id": "123",
        "model_params": {
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
    }

    # Создаем обработчик запросов для API
    handler = FastApiHandler()

    # Делаем тестовый запрос
    response = handler.handle(test_params)
    print(f"Response: {response}")