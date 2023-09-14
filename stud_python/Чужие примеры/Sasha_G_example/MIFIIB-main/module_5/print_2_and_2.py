"""Задание 5.1.1
Задание на самопроверку.

Напишите функцию print_2_add_2, которая будет складывать 2 плюс 2
и печатать этот результат. Не забудьте вызвать функцию, чтобы увидеть
результат."""


def print_2_and_2(num1, num2) :
    multiplication = num1 * num2
    return multiplication


print("Результат этих сложнейших вычислений = ", print_2_and_2(2, 2))


print('*' * 25, "Задание 5.1.2, функция для печати Hello World ")
def hello_world() :
    print("Hello World")

# Вызов функции
hello_world()
