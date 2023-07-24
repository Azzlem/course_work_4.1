import json
from abc import ABC


# Класс Вакансий
class MakeVacancies:
    def __init__(self, name: str, platform: str, responsibility: str, url: str, city, pay: dict = None,
                 requirement: str = "Не указано",
                 value: str = "Не указано"):
        self.name = name
        self.platform = platform
        self.responsibility = responsibility
        self.url = url
        self.city = city
        self.salary = pay
        self.requirement = requirement
        self.value = value

    @staticmethod
    def get_vacancies_from_file():
        """
        Получение вакансий из файлов и инициализация экземпляров класса
        :return: Список экземпляров класса
        """
        items = []
        for page in range(0, 20):
            with open(f"{page}.json", "r", encoding="utf-8") as file_hh:
                json_hh_file = json.load(file_hh)
                for item_hh in json_hh_file["items"]:
                    items.append(MakeVacancies(
                        item_hh["name"],
                        "HeadHunter",
                        item_hh["snippet"]["responsibility"],
                        item_hh["alternate_url"],
                        item_hh["area"]["name"],
                        item_hh["salary"]["from"] if isinstance(item_hh["salary"], dict) else "Не указана",
                        item_hh["snippet"]["requirement"],
                        item_hh["salary"]['currency'] if isinstance(item_hh["salary"], dict) else "Не указана"

                    ))

        for page in range(0, 5):
            with open(f"{page}_SJ.json", "r", encoding="utf-8") as file_sj:
                json_sj_file = json.load(file_sj)
                for item_sj in json_sj_file["objects"]:
                    items.append(MakeVacancies(
                        item_sj["profession"],
                        "SuperJob",
                        item_sj["candidat"],
                        item_sj["link"],
                        item_sj["town"]["title"],
                        item_sj["payment_from"],
                        item_sj["vacancyRichText"],
                        item_sj["currency"]

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


# Класс родитель для работы с файлом хранения вакансий
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


# Класс для работы с файлом хранения вакансий
class VacanciesJson(Vacancies):
    """
    Класс для записи вакансий в файл, чления вакансий из файлав и очистки файла
    """
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

        with open("vacancy.json", "w", encoding="utf-8") as file:
            json.dump(vacancies_to_file, file)

    @staticmethod
    def get_vacancies():
        with open("vacancy.json", "r", encoding="utf-8") as file:
            template = json.load(file)
        return template

    @staticmethod
    def del_vacancies():
        with open("vacancy.json", "w", encoding="utf-8") as file:
            pass
