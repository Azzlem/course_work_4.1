import json


# Функция сортировки по городу
def city(user_city):
    with open("vacancy.json", "r") as file:
        template = json.load(file)

    data_user_seach = []

    for vacancy in template:
        if vacancy["city"] == user_city:
            data_user_seach.append(vacancy)

    return data_user_seach


# Функция сортировки по зарплате
def salary(user_salary):
    with open("vacancy.json", "r") as file:
        template = json.load(file)

    data_user_seach = []

    for vacancy in template:
        if isinstance(vacancy["salary"], int) and vacancy["salary"] >= int(user_salary):
            data_user_seach.append(vacancy)

    return data_user_seach


# Функция сортировки по названию вакансии
def word(user_word):
    with open("vacancy.json", "r") as file:
        template = json.load(file)

    data_user_seach = []

    for vacancy in template:
        if user_word in vacancy["name"]:
            data_user_seach.append(vacancy)

    return data_user_seach


# Функция сортировки: по городу, названию вакансии и зарплате.
def mix_seach(city_user_input, user_word_input, user_salary_input):
    with open("vacancy.json", "r") as file:
        template = json.load(file)

        data_user_seach = []
        for vacancy in template:
            if user_word_input in vacancy["name"]:
                if isinstance(vacancy["salary"], int) and vacancy["salary"] >= int(user_salary_input):
                    if vacancy["city"] == city_user_input:
                        data_user_seach.append(vacancy)
        return data_user_seach
