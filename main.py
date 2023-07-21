from utils import platform_func, pay_func, vacancy_func

platform = input("Нажмите 1 для HeadHunter или 2 для Superjob или 3 для обоих платформ: ")
choise_platform = input("Вывести информацию о вакансиях? yes/no: ")

if choise_platform == "yes":
    temp_platform = platform_func(platform)
    for el_platform in temp_platform:
        print(el_platform)

pay = input("Введите желаемую зарплату: ")
choise_pay= input("Вывести информацию о вакансиях? yes/no: ")

if choise_pay == "yes":
    temp_pay = pay_func(pay)
    for el_pay in temp_pay:
        print(el_pay)

name_of_vacancy = input("Введите имя вакансию: ")
choise_vacancy = input("Вывести информацию о вакансиях? yes/no: ")

if choise_vacancy == "yes":
    temp_vacancy = vacancy_func(name_of_vacancy)
    if temp_vacancy is None:
        print("Нет вакансий с таким именем!")
    else:
        for el_vacancy in temp_vacancy:
            print(el_vacancy)


