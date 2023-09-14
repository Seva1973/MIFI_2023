# Данный вариант игры реализуется в консоли, каждый ход выводит заново поле с добавленным
# элементом Х или О
from colorama import init as colorama_init
from colorama import Fore, Style

# глобальные переменные
# сетку игры (grid) в текстовом формате игры легче пронумеровать, для того, чтобы игрок мог указать
# номер выбранной клетки для хода

# глобальные переменные
grid = list(range(1, 10))
turn = "X"
won = False


print("\nНачинаем игру в крестики-нолики\n")
print("Игровое поле: ")
# фунцкия выводящая игровое поле на экран терминала
def draw_game(grid) :
    colorama_init()
    print(f"{Fore.LIGHTYELLOW_EX}")  # игральное поле светло-желтого цвета
    print("-" * 13)
    for i in range(3) :
        print("|", grid[0 + i * 3], "|", grid[1 + i * 3], "|", grid[2 + i * 3], "|")
        print("-" * 13)
    print(f"{Style.RESET_ALL}")


# функция для определения и перехода хода к следующему игроку
# def switch_turn() :
#     global turn
#     if turn == "X" :
#         turn = "О"
#     else :
#         turn = "X"
#     print("Следующий игрок: " + turn)


# проверка выигрышных позиций, возвращает 'True' если игрок выиграл, 'False' если наоборот
def check_win(grid) :
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord :
        if grid[each[0]] == grid[each[1]] == grid[each[2]] :
            return grid[each[0]]
    return False


def take_input(turn) :
    valid = False  # проверка доступности клетки для хода
    while not valid :
        player_answer = input("Куда поставим " + turn + "? Выбирайте номер --> \t")
        try :
            player_choice = int(player_answer)
        except :
            print("Неверный ввод, введите число от 1 до 9")
            continue
        if 1 <= player_choice <= 9 :
            if (str(grid[player_choice - 1]) not in "XO") :
                grid[player_choice - 1] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
                valid = True
                # switch_turn()
            else :
                print("Эта клеточка уже занята")
        else :
            print("Неверный ввод, введите число от 1 до 9")


def main(grid) :
    global won
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
                # reset()
                break
        if counter_moves == 9 :
            print("Ничья!")
            break


# перезагрузка игры по окончании
# def reset() :
#     global grid, turn, won
#     grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#     turn = "X"
#     won = False
#     print("Игровое поле: ")
#     print("Начинаем игру с крестика " + turn)
#     draw_game(grid)


main(grid)

# print("\n********************* testing selection...\n")
# grid[0][0] = f"{Fore.RED}Х{Fore.LIGHTYELLOW_EX}"
# grid[1][1] = f"{Fore.RED}O{Fore.LIGHTYELLOW_EX}"
# grid[2][2] = f"{Fore.RED}" + turn + f"{Fore.LIGHTYELLOW_EX}"
# draw_game(grid)
