# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# ** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func1(x, y):
    return x ** y


def my_func2(x, y):
    counter = 1
    result = 1 * x

    while counter < abs(y):
        result = result * (1 * x)
        counter += 1
    return result

print(f'Вариант №1, с оператором **: {my_func1(int(input("Введите Х: ")), int(input("Введите У: ")))}')

print(f'Вариант №2, без оператором **: {my_func2(int(input("Введите Х: ")), int(input("Введите У: ")))}')

