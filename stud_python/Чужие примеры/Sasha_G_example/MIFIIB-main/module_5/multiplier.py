def multiplier(*nums) :
    mult_ = 1
    for n in nums :
        mult_ *= n

    return mult_


print(multiplier())  # теоретически, не стоит задзвать функции 0 аргументов...
print(multiplier(1))
print(multiplier(1, 2))
print(multiplier(4, 9, 8))
print(multiplier(1, 4, 11, 123, 565, 4311))
