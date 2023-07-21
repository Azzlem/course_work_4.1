from abc import ABC

import requests


class GetJson(ABC):

    @staticmethod
    def get_json_to_file():
        pass


class GetJsonHH(GetJson):

    @staticmethod
    def get_json_to_file():
        params = {
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно

        with open("text.json", "w") as f:
            f.write(data)

        req.close()


class GetJsonSJ(GetJson):
    @staticmethod
    def get_json_to_file():
        pass
