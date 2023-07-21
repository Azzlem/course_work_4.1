from get_json import GetJsonHH
from vacancies import MakeVacancies

GetJsonHH.get_json_to_file()
items = MakeVacancies.get_vacancies_from_file()


def platform_func(platform):
    data = []
    for item in items:
        data.append(item.__repr__())

    return data


def pay_func(pay):
    data = []
    for item in items:
        if isinstance(item.salary, int) and int(pay) <= int(item.salary):
            data.append(item.__repr__())

    return data


def vacancy_func(name_of_vacancy):
    data = []
    for item in items:
        if name_of_vacancy in item.name:
            data.append(item.__repr__())
