import requests
import argparse


def do_fuzzing(site, directories):

    for directory in directories:
        response = requests.get(f'{site}/')
        # print(type(response.status_code))
        if response.status_code == 200:
            print(response.status_code)


# parse from the existing file in the current module_6 directory
# we can load up a large file to parse to get the data we need
# with open('files_to_open/file_passwords.txt') as f:
#     file = f.read().split('\n')
# print(file)

file = ['f1', 'f2', 'f3']

parser = argparse.ArgumentParser(description='Fuzzer')
parser.add_argument('site', help='Site for fuzzing')
args = parser.parse_args()
print(file)
do_fuzzing(args.site, file)

# запуск из терминала: python3 nikolai_fuzzer_v1.py https://ya.ru
# help: python3 nikolai_fuzzer_v1.py -h