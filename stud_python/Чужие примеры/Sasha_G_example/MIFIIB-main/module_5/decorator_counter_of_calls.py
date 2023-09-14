"""Задание 5.4.2
Задание на самопроверку.

Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
Для хранения переменной, содержащей количество вызовов, используйте nonlocal область декоратора."""


def my_func_decorator(func) :
    counter = 0

    def wrapper(*args, **kwargs) :
        nonlocal counter
        func(*args, **kwargs)
        counter += 1
        print(f"Функция {func} была вызвана {counter} раз")
    return wrapper


@my_func_decorator
def my_func(my_string):
    print(my_string)


my_func("Hi people!")
my_func("That's me again!")
my_func("Is there anybody here?")


"""def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    def wrapper(*args, **kwargs):
        print("Этот код будет выполняться перед каждым вызовом функции")
        result = fn(*args, **kwargs)
        print("Этот код будет выполняться после каждого вызова функции")
        return result
    return wrapper"""
