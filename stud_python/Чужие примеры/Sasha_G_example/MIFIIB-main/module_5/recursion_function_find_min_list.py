"""Задание 5.5.9
Задание на самопроверку.

Напишите рекурсивную функцию, находящую минимальный элемент списка без использования
циклов и встроенной функции min()."""


def recursive_func_min(list_):

    if len(list_) == 1 :
        return list_[0]
    return list_[0] if list_[0] < recursive_func_min(list_[1 :]) else recursive_func_min(list_[1 :])


my_string = input("Введите список натуральных чисел через пробел: \n")

list_of_numbers = list(map(int, my_string.split())) # список чисел
print("Введённый список чисел: ", list_of_numbers)


print(recursive_func_min(list_of_numbers))
