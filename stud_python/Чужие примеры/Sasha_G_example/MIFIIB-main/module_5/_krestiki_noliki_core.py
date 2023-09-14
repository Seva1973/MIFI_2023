# board = list(range(1,10))
# print(board)
# L = [ a for a in list(range(0, 9)) ]
# print(L)
from colorama import init as colorama_init
from colorama import Fore

grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
turn = "X"
won = False


# print(grid)
# print(grid[1][0])


def draw_game(grid) :
    colorama_init()
    print(f"{Fore.LIGHTYELLOW_EX}")

    # print('-' * 13)
    # for i in range(3) : # индекс строки
    #     for j in range(3) : # индекс колонки
    #         print('|', grid[i][j], end=" ")
    #     print('|') # перенос на новую строку
    # print('-' * 13)
    # вариант "пустой" доски, где будут рисоваться Х и 0
    for i in range(3) :  # индекс строки
        print('-' * 13)
        for j in range(3) :  # индекс колонки
            print('|', ' ', end=" ")
        print('|')  # перенос на новую строку
    print('-' * 13)


def switch_turn() :
    global turn
    if turn == "X" :
        turn = "O"
    else :
        turn = "X"
    print("Следующий игрок: " + turn)


print("Начинаем игру в крестики-нолики...\n")
print("Игровое поле -->")
draw_game(grid)
