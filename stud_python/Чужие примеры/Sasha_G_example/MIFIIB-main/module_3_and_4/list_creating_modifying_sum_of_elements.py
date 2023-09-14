"""
Задание 3.9.4
Напишите программу, которая на вход получает последовательность чисел,
а выводит модифицированный список:

Первое и последнее числа последовательности должны поменяться местами.
В конец списка нужно добавить сумму всех чисел."""
string = input("Введите числа через пробел: ")

list_of_strings = string.split() # список строковых представлений чисел
list_of_strings = list(map(int, list_of_strings)) # список чисел
print(list_of_strings)
print("Меняем местами первый и последний элементы: ") # множественное присваивание
list_of_strings[0], list_of_strings[len(list_of_strings) - 1] = list_of_strings[len(list_of_strings) - 1], list_of_strings[0]
print(list_of_strings)
print("Вычисляем сумму всех элементов, заносим её в конец списка: ")
last_elem_sum = sum(list_of_strings)
list_of_strings.append(last_elem_sum)
print(list_of_strings)

