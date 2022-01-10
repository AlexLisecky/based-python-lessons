# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
# x = x / x ** 2

def my_func(x, y):
    return 1 / (x ** abs(y))


print(my_func(4, -2))
# результат 0.0625


def my_func_2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


print(my_func_2(4, -2))
# результат 0.0625, реализация через цикл for in


def my_func_3(x, y):
    i = 1
    result = 1
    while i <= abs(y):
        result *= x
        i += 1
    return 1 / result


print(my_func_3(4, -2))
# результат 0.0625,реализация через цикл while
