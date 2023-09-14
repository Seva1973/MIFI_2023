"""Задание 5.3.1
Задание на самопроверку.

Создать функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
По умолчанию она начинается с единицы и шаг равен 1, но пользователь может указать любой
шаг и любое число в качестве аргумента функции, с которого будет начинаться последовательность."""


def sequence_natural_nums(n = 1, step = 1):
    sequence = n
    while True:
        yield sequence
        sequence += step

number = int(input("Введите ваше число: "))
step_user = int(input("Введите шаг: "))
for number in sequence_natural_nums(number, step_user):
    print(number)