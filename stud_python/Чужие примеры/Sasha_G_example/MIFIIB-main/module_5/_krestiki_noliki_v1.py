# Данный вариант игры реализуется в консоли, каждый ход выводит заново поле с добавленным
# элементом Х или О

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


def take_input(player_move) :
    valid = False # проверка доступности клетки для хода
    while not valid :
        player_answer = input("Куда поставим " + player_move + "? ")
        try :
            player_answer = int(player_answer)
        except :
            print("Неверный ввод, введите число от 1 до 9")
            continue
        if 1 <= player_answer <= 9 :
            # этот элемент надо вывести в отдельную функцию...
            if str(grid[player_answer - 1]) not in "XO" :
                grid[player_answer - 1] = player_move
                valid = True
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
    print("Начинаем игру с крестика " + turn)


print("Начинаем игру в крестики-нолики...\n")
print("Игровое поле: ")
draw_game(grid)


grid[0][0] = f"{Fore.RED}Х{Fore.LIGHTYELLOW_EX}"
grid[1][1] = f"{Fore.RED}O{Fore.LIGHTYELLOW_EX}"
print(grid)
print(grid[1])
draw_game(grid)
