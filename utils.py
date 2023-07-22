import json

from get_json import GetJsonHH
from vacancies import MakeVacancies, VacanciesJson

# GetJsonHH.page_to_json()
# items = MakeVacancies.get_vacancies_from_file()
# VacanciesJson.add_vacancies()
with open("creepy.json", "r") as file:
    template = json.load(file)


# for el in template:
#     if isinstance(el["salary"], int) and int(el["salary"]) >= 100000:
#         if el["name"].find("python") or el["requirement"].find("python") or el["responsibility"].find("python"):
#             print(el)


def user_input():
    city = input("1")
    if input("Нажмите 0 что остановить поиск и вывести результат: ") == "0":
        return [city]
    else:
        name = input("2").split()
        if input("Нажмите 0 что остановить поиск и вывести результат: ") == "0":
            return [city, name]
        else:
            pay = int(input("3"))
            if input("Нажмите 0 что остановить поиск и вывести результат: ") == "0":
                return [city, name, pay]
            else:
                skills = input("4").split()
                return [city, name, pay, skills]


def seach():
    total_user_input = user_input()
    print(total_user_input)
    total_all = []

    for el in template:
        total = [
            el["city"],
            el["name"],
            el["url"],
            el["salary"],
            el["currency"],
            el["requirement"],
            el["responsibility"]
        ]
        if len(total_user_input) == 1 and el["city"] == total_user_input[0]:
            total_all.append(total)
        elif len(total_user_input) == 2 and el["city"] == total_user_input[0] and any(
                item in el["name"] for item in total_user_input[1]):
            total_all.append(total)
        elif len(total_user_input) == 3 and el["city"] == total_user_input[0] and any(
                item in el["name"] for item in total_user_input[1]) and isinstance(
            el["salary"], int) and int(el["salary"]) > total_user_input[2]:
            total_all.append(total)
        elif len(total_user_input) == 3 and el["city"] == total_user_input[0] and any(
                item in el["name"] for item in total_user_input[1]) and isinstance(
            el["salary"], int) and el["salary"] > total_user_input[2] and any(
            it in el["responsibility"] for it in total_user_input[4]):
            total_all.append(total)
    return total_all
