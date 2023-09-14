"""
Задание 5.5.11
Задание на самопроверку.
Поработаем над более сложной рекурсивной функцией. Сейчас попробуем реализовать функцию equal(N, S),
проверяющую, совпадает ли сумма цифр числа N с числом S. При написании программы следует обратить
внимание на то, что, если S стала отрицательной, то необходимо сразу вернуть False.
Реализуйте описанную выше функцию."""


def equal(N, S) :
    if S < 0 :
        return False
    if N == S:
        return True
    else :
        return False


def sum_digit(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digit(n // 10)


my_number = int(input("Введите натуральное число состоящее из n цифр: \n"))
number_s = int(input("Введите некое число S: \n"))
my_number_sum = sum_digit(my_number)
print("Сумма цифр введённого числа = ", my_number_sum)

print("Равны ли N и S? ", equal(my_number_sum, number_s))

