import json
import os
from datetime import datetime

from src.get_json import GetJsonHH, GetJsonSJ
from src.vacancies import MakeVacancies, VacanciesJson
from src.utils import city, salary, word, mix_seach

GetJsonHH.page_to_json()
GetJsonSJ.page_to_json()
items = MakeVacancies.get_vacancies_from_file()

VacanciesJson.add_vacancies()

# Тело основного цикла взаимодействия с пользователем
while True:
    command = input(
        "Отсортировать по городу нажмите 1\n"
        "Отсортировать по зарплате нажмите 2\n"
        "Отсортировать по названию вакансии нажмите 3\n"
        "Нажмите 4 если вы хотите использовать все фильтры\n"
        "Выйти - введите 'stop'\n"
    )
    if command.lower() == "stop":
        break
    elif command == "1":
        city_user = input("Введите город: ").capitalize()
        temp_list_city = city(city_user)
        for vacancy_city in temp_list_city:
            print(f"Вакансия\n"
                  f"Ссылка на вакансию: {vacancy_city['url']}\n"
                  f"Название вакансии: {vacancy_city['name']}\n"
                  f"Обязанности: {vacancy_city['responsibility']}\n"
                  f"Зарплата от: {vacancy_city['salary']}\n")

        with open(f"../course_work_4.1/result_json/{city_user}{datetime.today()}.json", "w") as file:
            json.dump(temp_list_city, file)

    elif command == "2":
        user_salary = input("Введите желаемую зарплату: ")
        if not user_salary.isdigit():
            raise Exception("Вы ввели не цифру!")
        else:
            temp_list_salary = salary(user_salary)
            for vacancy_salary in temp_list_salary:
                print(f"Вакансия\n"
                      f"Ссылка на вакансию: {vacancy_salary['url']}\n"
                      f"Название вакансии: {vacancy_salary['name']}\n"
                      f"Обязанности: {vacancy_salary['responsibility']}\n"
                      f"Зарплата от: {vacancy_salary['salary']}\n")

            with open(f"../course_work_4.1/result_json/{user_salary}_{datetime.today()}.json", "w") as file:
                json.dump(temp_list_salary, file)

    elif command == "3":
        user_word = input("Введите название вакансии: ")
        temp_list_word = word(user_word)
        for vacancy_word in temp_list_word:
            print(f"Вакансия\n"
                  f"Ссылка на вакансию: {vacancy_word['url']}\n"
                  f"Название вакансии: {vacancy_word['name']}\n"
                  f"Обязанности: {vacancy_word['responsibility']}\n"
                  f"Зарплата от: {vacancy_word['salary']}\n")

        with open(f"../course_work_4.1/result_json/{user_word}{datetime.today()}.json", "w") as file:
            json.dump(temp_list_word, file)

    elif command == "4":
        city_user_input = input("Введите город: ").capitalize()
        user_word_input = input("Введите название вакансии: ")
        user_salary_input = input("Введите желаемую зарплату: ")
        if not user_salary_input.isdigit():
            raise Exception("Вы ввели не цифру!")
        else:
            temp_list_result = mix_seach(city_user_input, user_word_input, user_salary_input)
            for vacancy_mix_seach in temp_list_result:
                print(f"Вакансия\n"
                      f"Ссылка на вакансию: {vacancy_mix_seach['url']}\n"
                      f"Название вакансии: {vacancy_mix_seach['name']}\n"
                      f"Обязанности: {vacancy_mix_seach['responsibility']}\n"
                      f"Зарплата от: {vacancy_mix_seach['salary']}\n")

            with open(f"../course_work_4.1/result_json/{city_user_input}_"
                      f"{user_word_input}_{user_salary_input}_{datetime.today()}.json", "w") as file:
                json.dump(temp_list_result, file)

# Удаааление временных файлов и очистка экземпляров класса
VacanciesJson.del_vacancies()
for _ in range(0, 20):
    os.remove(f"{_}.json")
for el in range(0, 5):
    os.remove(f"{el}_SJ.json")
os.remove("vacancy.json")

