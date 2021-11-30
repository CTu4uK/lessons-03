# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(first_name, last_name, birth, sity, email, tel):
    return print(f"Имя: {first_name}, Фамилия: {last_name},Год рождения: {birth}, "
                 f"Город проживания: {sity}, E-Mail: {email}, Телефон: {tel}")

user_data(
    first_name = input("Имя: "),
    last_name = input("Фамилия: "),
    birth = input("Год рождения: "),
    sity = input("Город проживания: "),
    email = input("E-Mail: "),
    tel = input("Телефон: "),
)