import requests


site = str(input("Enter your site here: "))
directories = ['password', 'logins', 'inputs']

for directory in directories:
    response = requests.get(f'{site}/')
    # print(type(response.status_code))
    if response.status_code == 200:
        print(response.status_code)

# response 1
# Enter your site here: https://ya.ru/
# <Response [404]>
# <Response [404]>
# <Response [404]>

# then after the modification (type)
# <class 'int'>
# <class 'int'>
# <class 'int'>



