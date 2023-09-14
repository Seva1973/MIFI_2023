my_string = input("Введите пожалуйста строку: \n")


def reverse_string(my_string) :
    if len(my_string) == 0 :
        return ''
    else :
        return my_string[-1] + reverse_string(my_string[:-1])


print("Выделение последнего элемента: ", my_string[-1])
print("Выделение всей строки без последнего элемента: ", my_string[:-1])
print("Вариант без рекурсии: ", my_string[: :-1])
print("Вариант с рекурсией: ", reverse_string(my_string))
