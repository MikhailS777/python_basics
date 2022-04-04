"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


# функция выводит результат деления двух чисел
def delenie_chisel(a, b):
    try:
        print(f"Результат деления {a} на {b} = {a / b}")
    except ZeroDivisionError:
        print("Деление на ноль!")


a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
delenie_chisel(a, b)
