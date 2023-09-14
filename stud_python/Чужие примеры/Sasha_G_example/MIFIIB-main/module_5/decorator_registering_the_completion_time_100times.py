"""Задание 5.4.1
Задание на самопроверку.

Взять из предыдущего примера декорированные функции, которые возвращают время работы основной функции,
и найти среднее время выполнения для 100 выполнений каждой функции."""
import time

N = 100


def decorator_time(fn) :
    def wrapper() :
        # print(f"Запустилась функция {fn}")
        t0 = time.time()
        # result = fn() # эта строка выводит результат вычисления pow_2() и in_build_pow()
        # print(f"Результат шычисления переданной функции {fn}", result)
        dt = time.time() - t0
        # print(f"Функция выполнилась. Время: {dt:.10f}")
        return dt  # задекорированная функция будет возвращать время работы

    return wrapper


def pow_2() :
    return 10000000 ** 2


def in_build_pow() :
    return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

mean_pow_2 = 0 # добавили переменную среднего значения и присвоили ей нулевое значение
mean_in_build_pow = 0
for _ in range(N): # _ перебирает итерируемые элементы, чтобы не использовать индекс
    mean_pow_2 += pow_2()
    mean_in_build_pow += in_build_pow()

print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")
