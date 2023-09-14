def my_func(*args, **kwargs):
   print(type(args))
   print(type(kwargs))

my_func()
# <class 'tuple'>
# <class 'dict'>

print('*' * 25)
a = [1, 2, 3]
b = [a, 4, 5, 6]
print(b)
# [[1, 2, 3], 4, 5, 6]

a = [1, 2, 3]
b = [*a, 4, 5, 6] # распаковываем элементы списка а, не вставляем список
print(b)
# [1, 2, 3, 4, 5, 6]