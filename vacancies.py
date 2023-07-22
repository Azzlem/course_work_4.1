import json
from abc import ABC


class MakeVacancies:
    def __init__(self, name: str, platform: str, responsibility: str, url: str, city, pay: dict = None, requirement: str = "Не указано",
                 value: str = "Не указано"):
        self.name = name
        self.platform = platform
        self.responsibility = responsibility
        self.url = url
        self.city = city
        self.salary = pay["from"] if isinstance(pay, dict) else "Не указана"
        self.requirement = requirement
        self.value = f"{value['currency']}" if isinstance(pay, dict) else "Не указана"

    @staticmethod
    def get_vacancies_from_file():
        items = []
        for page in range(0, 20):
            with open(f"{page}.json", "r", encoding="utf-8") as f:
                json_file = json.load(f)
                for item in json_file["items"]:
                    items.append(MakeVacancies(
                        item["name"],
                        "HeadHunter",
                        item["snippet"]["responsibility"],
                        item["alternate_url"],
                        item["area"]["name"],
                        item["salary"],
                        item["snippet"]["requirement"],
                        item["salary"]

                    ))

        return items

    def __repr__(self):
        return f"{self.name}\n" \
               f"Зарплата: От {self.salary}\n" \
               f"{self.requirement}\n" \
               f"{self.url}"

    def __ge__(self, other):
        """
        Метод сравнения зарплат
        """
        return int(
            self.salary[3:]
        ) >= int(
            other.salary[3:]
        ) if isinstance(
            self.salary, str
        ) and isinstance(
            other.salary, str
        ) else "Зарплата одной из вакансий не указана"


class Vacancies(ABC):
    @staticmethod
    def add_vacancies():
        pass

    @staticmethod
    def del_vacancies():
        pass

    @staticmethod
    def get_vacancies():
        pass


class VacanciesJson(Vacancies):
    @staticmethod
    def add_vacancies():
        vacancies_to_file = []
        for el in MakeVacancies.get_vacancies_from_file():
            vacancies_to_file.append({
                "platform": el.platform,
                "url": el.url,
                "name": el.name,
                "salary": el.salary,
                "requirement": el.requirement,
                "currency": el.value,
                "city": el.city,
                "responsibility": el.responsibility
            })
        with open("creepy.json", "w", encoding="utf-8") as file:
            json.dump(vacancies_to_file, file)

    @staticmethod
    def get_vacancies():
        with open("creepy.json", "r", encoding="utf-8") as file:
            template = json.load(file)
        return template

    @staticmethod
    def del_vacancies():
        with open("creepy.json", "w", encoding="utf-8") as file:
            json.dump([], file)
