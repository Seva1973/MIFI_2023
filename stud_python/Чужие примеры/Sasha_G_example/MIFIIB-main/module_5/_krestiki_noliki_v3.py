# Данный вариант игры реализуется в консоли, каждый ход выводит заново поле с добавленным
# элементом Х или О
from unittest import case

from colorama import init as colorama_init
from colorama import Fore

# глобальные переменные
# сетку игры (grid) в текстовом формате игры легче пронумеровать, для того, чтобы игрок мог указать
# номер выбранной клетки для хода

# глобальные переменные
grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
turn = "X"
won = False


# фунцкия выводящая игровое поле на экран терминала
def draw_game(grid):
    colorama_init()
    print(f"{Fore.LIGHTYELLOW_EX}")  # игральное поле светло-желтого цвета
    # вариант "пустой" доски, где будут рисоваться Х и 0
    for i in range(3) :  # индекс строки
        print('-' * 13)
        for j in range(3) :  # индекс колонки
            print('|', grid[i][j], end=" ")
        print('|')  # перенос на новую строку
    print('-' * 13)


# функция для определения и перехода хода к следующему игроку
def switch_turn() :
    global turn
    if turn == "X" :
        turn = "О"
    else :
        turn = "X"
    print("Следующий игрок: " + turn)


# проверка выигрышных позиций, возвращает 'True' если игрок выиграл, 'False' если наоборот
def check_win() :
    for a in range(0, 3) :
        if grid[a][0] != " " and grid[a][0] == grid[a][1] == grid[a][2] :
            return True
    for b in range(0, 3) :
        if grid[0][b] != " " and grid[0][b] == grid[1][b] == grid[2][b] :
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " " :
        return True
    elif grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != " " :
        return True
    else :
        return False


def player_choice_match_cell(choice):
    global grid, turn
    match choice :
        case 1 :
            grid[0][0] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
        case 2 :
            grid[0][1] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
        case 3 :
            grid[0][2] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
        case 4 :
            grid[1][0] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
        case 5 :
            grid[1][1] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
        case 6 :
            grid[1][2] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
        case 7 :
            grid[2][0] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
        case 8 :
            grid[2][1] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
        case 9 :
            grid[2][2] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"


def take_input(turn) :
    colorama_init()
    valid = False # проверка доступности клетки для хода
    while not valid :
        player_answer = input("Куда поставим " + turn + "? Выбирайте номер --> \t")
        try :
            player_choice = int(player_answer)
        except :
            print("Неверный ввод, введите число от 1 до 9")
            continue
        if 1 <= player_choice <= 9 :
            if player_choice_match_cell(player_choice) not in "XO" :

                valid = True
                switch_turn()
            else :
                print("Эта клеточка уже занята")
        else :
            print("Неверный ввод, введите число от 1 до 9")


def main(grid) :
    global won, turn
    counter_moves = 0
    won = False
    while not won :
        draw_game(grid)
        if counter_moves % 2 == 0 :
            take_input("X")
        else :
            take_input("O")
        counter_moves += 1
        if counter_moves > 4 :
            check_win_status = check_win(grid)
            if check_win_status :
                print(check_win_status, f"{turn} выиграл!")
                won = True
                reset()
                break
        if counter_moves == 9 :
            print("Ничья!")
            reset()
            break
    draw_game(grid)


# перезагрузка игры по окончании
def reset() :
    global grid, turn, won
    grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turn = "X"
    won = False
    draw_game(grid)
    print("Начинаем игру с крестика " + turn)


print("Начинаем игру в крестики-нолики...\n")
print("Игровое поле: ")
draw_game(grid)

main(grid)
print("\n********************* testing selection...\n")
grid[0][0] = f"{Fore.RED}Х{Fore.LIGHTYELLOW_EX}"
grid[1][1] = f"{Fore.RED}O{Fore.LIGHTYELLOW_EX}"
grid[2][2] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
draw_game(grid)
