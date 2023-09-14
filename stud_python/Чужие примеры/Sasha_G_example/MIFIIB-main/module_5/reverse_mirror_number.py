"""
Задание 5.5.10
Задание на самопроверку.

Напишите рекурсивную функцию, которая зеркально разворачивает число. Предполагается, что число не содержит нули.
"""


def mirror_number(n):
    string_ = str(n)
    if len(string_) == 0 :
        return ''
    else:
        return string_[-1] + mirror_number(string_[:-1])


num = int(input("Введите ваше число: \n"))
print(mirror_number(num))

print('*' * 25, "Другой вариант")


def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res


num = int(input("Введите ваше число: \n"))
print(mirror(num))