"""
Задание 5.1.6
Задание на самопроверку.

Напишите функцию, которая проверяет, является ли данная строка палиндромом или нет, и возвращает
результат проверки. Пример:

check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True
"""


def check_palindrom(str_) :
    if str_ == (str_[: :-1]) :
        # return "Введенная строка - палиндром"
        return True
    else :
        # return "Строка не палиндром!"
        return False


# модифицируем условия задачи, добавляем новую функцию, которая переводит строки в нижний регистр,
# убирает пробелы и символы перевода на новую строку
def modify_string_lower_no_space(str_passed) :
    str_passed = str_passed.lower()
    str_passed = str_passed.replace(" ", "")
    str_passed = str_passed.replace("\n", "")
    return check_palindrom(str_passed)


entered_string = input("Введите вашу строку - ")
print(modify_string_lower_no_space(entered_string))
print(modify_string_lower_no_space("test"))
print(modify_string_lower_no_space("Кит на море не романтик"))
