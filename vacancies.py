import json
from abc import ABC

import requests


class Vacancies(ABC):
    @classmethod
    def make_vacancies(cls):
        pass

    @staticmethod
    def get_json_to_file():
        pass


class VacanciesAll(Vacancies):
    def __init__(self, platform, name, pay, city, responsibility, url, requirement):
        self.platform = platform
        self.name = name
        self.pay = f'От {pay["from"]}' if isinstance(pay, dict) else "Не указана"
        self.city = city
        self.responsibility = responsibility if isinstance(responsibility, str) else "Не указано"
        self.url = url
        self.requirement = requirement

    def __repr__(self):
        return f"{self.platform}: {self.url} : {self.pay}"

    @classmethod
    def make_vacancies(cls):
        items = []
        for item in json.loads(VacanciesAll.get_json_to_file_hh())["items"]:
            items.append(
                VacanciesAll(
                    "HeadHunter",
                    item["name"],
                    item["salary"],
                    item["area"]["name"],
                    item["snippet"]["responsibility"],
                    item["alternate_url"],
                    item["snippet"]["requirement"]
                )
            )

        return items

    @staticmethod
    def get_json_to_file_hh():
        params = {
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно

        with open("text.json", "w") as f:
            f.write(data)

        req.close()

        return data
