# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, 2, 3, False, 4.567, 3.1213, None, "test"]

for i in my_list:
    print(f'Тип этого элемента списка: "{i}" {type(i)}')
