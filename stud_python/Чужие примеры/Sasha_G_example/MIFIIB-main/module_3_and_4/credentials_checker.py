"""
Задание 4.4.4
Напишите программу, которая сначала запрашивает логин пользователя, проверяет, существует он или нет,
а потом с помощью вложенного условия проверяет пароль этого пользователя."""

login_list = [
   'root',
   'username1'
   ]

password_list = {
   'root': '1q2w3e4r',
   'username1': 'qwerty123'
}

username = input('Введите логин:\n')

# здесь допишите условие проверки логина и пароля
if username in login_list:
    password = input('Enter your password:\n')
    if password in password_list.values():
        # alternatively: if password_list[username] == password:
        print('Login successful!')
    else:
        print('Access denied!')
else:
    print('Wrong login! Try again.')


