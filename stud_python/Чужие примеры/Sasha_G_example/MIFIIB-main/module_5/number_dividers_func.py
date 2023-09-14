"""Задание 5.1.5
Задание на самопроверку.
Напишите функцию, которая будет возвращать количество делителей числа а.

Пример ввода: 5
Пример вывода программы: 2"""


def check_num(num) :
    count = 0
    for n in range(1, num + 1):
        if num % n == 0 :
            count += 1
    return count


choice = ''
# Начинаем цикл с проверкой опции на выход из программы.
while choice != 'q' :
    # Здесь настраивается возможность выбора пользователя
    print("\n[a] Наберите a чтобы ввести ваше число")
    print("[q] Введите q для выхода из программы")

    # Ask for the user's choice.
    choice = input("\nВаш выбор?\n")

    # Respond to the user's choice.
    if choice == 'a' :

        num = int(input("Введите ваше число: \n"))
        print("Количество делителей этого числа = ", check_num(num))

    elif choice == 'q' :
        print("\nВыход из игры...\n")
        break
    else :
        print("\nЭта опция не была предусмотрена. Проверьте, если у вас включена английская раскладка.\n")

# Print a message that we are all finished.
print("Спасибо за ваше время, до новых встреч!")



