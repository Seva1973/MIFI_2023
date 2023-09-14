# Короткое вводное слово для пользователя.
print("\nЗдесь мы вводим двузначные и трёхзначные числа и проверяем, если в них присутствует цифра 5. \n"
      "Есть три выбора:  \n"
      "a - двузначноe числo\n"
      "b - трёхзначноe числo\n"
      "q - выход из программы")

# Начальное значение выбора
choice = ''


# Функция для вывода кортежа набранных цифр
def get_digits_from_left_to_right(number, lst=None) :
    """Return digits of an integer excluding the sign."""

    if lst is None :
        lst = list()

    number = abs(number)

    if number < 10 :
        lst.append(number)
        return tuple(lst)

    get_digits_from_left_to_right(number // 10, lst)
    lst.append(number % 10)

    return tuple(lst)


# Начинаем цикл с проверкой опции на выход из программы.
while choice != 'q ' :
    # Здесь настраивается возможность выбора пользователя
    print("\n[a] Введите a чтобы ввести двузначное число")
    print("[b] Введите b чтобы ввести трёхзначное число")
    print("[q] Введите q для выхода из программы")

    # Ask for the user's choice.
    choice = input("\nВаш выбор? ")

    # Respond to the user's choice.
    if choice == 'a' :
        num = int(input("Введите двузначное число --> "))
        digit1 = num // 10
        digit2 = num % 10
        print("Первая и вторая цифры:", str(digit1) + " и " + str(digit2))
        if (digit1 == 5) or (digit2 == 5) :
            print("Данное число содержит цифру 5!")
        else :
            print("Данное число не содержит цифру 5")

    elif choice == 'b' :
        num = int(input("Введите трёхзначное число --> "))
        num_converted_list = list((get_digits_from_left_to_right(num)))
        digit1 = int(num_converted_list[0])
        digit2 = int(num_converted_list[1])
        digit3 = int(num_converted_list[2])
        print("Первая, вторая и третья цифры:", str(digit1) + " и " + str(digit2) + " и " + str(digit3))
        if ((digit1 == 5) or (digit2 == 5)) or (digit3 == 5) :
            print("Данное число содержит цифру 5!")
        else :
            print("Данное число не содержит цифру 5")

    elif choice == 'q' :
        print("\nВыход из игры...\n")
        break
    else :
        print("\nЭта опция не была предусмотрена. Проверьте, если у вас включена английская раскладка.\n")

# Print a message that we are all finished.
print("Спасибо за игру, до новых встреч!")

# Для многозначных чисел, на будущее
# def get_digit(num):
#     if num < 10:
#         print(num)
#     else:
#         get_digit(num // 10)
#         print(num % 10)
# from math import floor, log10
#
# def digits(n):
#     """generator which returns digits in left to right order"""
#     k = floor(log10(n))
#     for e in range(k,-1,-1):
#         d,n = divmod(n,10**e)
#         yield d
