import json
import time
from abc import ABC

import requests


class GetJson(ABC):

    @staticmethod
    def get_json_to_file():
        pass


class GetJsonHH(GetJson):

    @staticmethod
    def get_page(page=0):
        params = {
            'page': page,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице

        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно

        req.close()
        return data

    @staticmethod
    def page_to_json():
        for page in range(0, 20):

            # Преобразуем текст ответа запроса в справочник Python
            json_page = json.loads(GetJsonHH.get_page(page))

            # Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
            # Определяем количество файлов в папке для сохранения документа с ответом запроса
            # Полученное значение используем для формирования имени документа
            next_file_name = f'{page}.json'

            # Создаем новый документ, записываем в него ответ запроса, после закрываем
            f = open(next_file_name, mode='w', encoding='utf8')
            f.write(json.dumps(json_page, ensure_ascii=False))
            f.close()

            # Проверка на последнюю страницу, если вакансий меньше 2000
            if (json_page['pages'] - page) <= 1:
                break

            # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
            time.sleep(0.25)


class GetJsonSJ(GetJson):
    @staticmethod
    def get_json_to_file():
        pass
