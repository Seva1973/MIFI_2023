string = input("Введите числа через пробел: ")

list_of_strings = string.split() # список строковых представлений чисел
list_of_strings = list(map(int, list_of_strings)) # список чисел

print(sum(list_of_strings[::3])) # sum() вычисляет сумму элементов

