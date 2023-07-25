import json
import time
from abc import ABC

import requests
from dotenv import dotenv_values


# Родительский класс для двух классов парсинга апи и записи результата в JSON
class GetJson(ABC):

    @staticmethod
    def get_page():
        pass

    @staticmethod
    def page_to_json():
        pass


# Класс работы с Апи HeadHunter
class GetJsonHH(GetJson):

    @staticmethod
    def get_page(page=0):
        """
        Статик метод парсинга вакансий HH
        :param page: номер страницы
        :return: результат парсинга
        """
        params = {
            'page': page,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице

        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        if req.status_code != 200:
            raise Exception("Сервер не отвечает. Ошибка запроса API")
        else:
            data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно

            req.close()

        return data

    @staticmethod
    def page_to_json():
        """
        Записывает результат парсинга в файл Json
        """
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


# Класс работы с Апи SuperJob
class GetJsonSJ(GetJson):
    @staticmethod
    def get_page(page=0):
        """
        Статик метод парсинга вакансий SJ
        :param page: номер страницы
        :return: результат парсинга
        """
        api_key_js = dotenv_values("values.env")["API_SJ"]
        headers = {
            "X-Api-App-Id": api_key_js,
        }
        params = {
            "count": 100,
            "page": page,
            "not_archive": True,
        }

        req = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        if req.status_code != 200:
            raise Exception("Сервер не отвечает. Ошибка запроса API")
        else:
            data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно

            req.close()
        return data

    @staticmethod
    def page_to_json():
        """
        Записывает результат парсинга в файл Json
        """
        for page in range(0, 5):

            # Преобразуем текст ответа запроса в справочник Python
            json_page = json.loads(GetJsonSJ.get_page(page))

            # Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
            # Определяем количество файлов в папке для сохранения документа с ответом запроса
            # Полученное значение используем для формирования имени документа
            next_file_name = f'{page}_SJ.json'

            # Создаем новый документ, записываем в него ответ запроса, после закрываем
            f = open(next_file_name, mode='w', encoding='utf8')
            f.write(json.dumps(json_page, ensure_ascii=False))
            f.close()

            # Проверка на последнюю страницу, если вакансий меньше 2000
            if (json_page['total'] - page) <= 1:
                break

            # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы можем подождать
            time.sleep(0.25)
