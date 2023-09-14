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
    print(f"{Fore.YELLOW}")  # игральное поле светло-желтого цвета
    print("-" * 13)
    for i in range(3) :
        print("|", grid[0 + i * 3], "|", grid[1 + i * 3], "|", grid[2 + i * 3], "|")
        print("-" * 13)
    print(f"{Style.RESET_ALL}")


def switch_turn():
    global turn
    if turn == "X": # никак не могу заставить печатать мои крестики и нолики в другом цвете, ломает всю логику,
        # т.е. программа пишет Х и О в то же самое поле...
        turn = "O"
    else:
        turn = "X"


def take_input(player_turn) :
    valid = False  # проверка доступности клетки для хода
    while not valid :
        player_answer = input("Куда поставим " + player_turn + "? Выбирайте номер --> \t")
        try :
            player_choice_num = int(player_answer)
        except :
            print("Неверный ввод, введите число от 1 до 9")
            continue
        if 1 <= player_choice_num <= 9 :

            if str(grid[player_choice_num - 1]) not in "XO" :
                grid[player_choice_num - 1] = player_turn
                valid = True
            else :
                print("Поле занято, выберите другое")

        else :
            print("Неверный ввод, введите число от 1 до 9")


def main(grid) :
    global won, turn
    counter_moves = 0
    won = False
    while not won:
        draw_game(grid)
        if counter_moves % 2 == 0 :
            take_input(turn)
            switch_turn()
        else :
            take_input(turn)
            switch_turn()
        counter_moves += 1
        if counter_moves > 4 :
            check_win_status = check_win(grid)
            switch_turn()
            if check_win_status :
                print(f"{turn} выиграл!")
                won = True
                break
            else:
                switch_turn()
        if counter_moves == 9 :
            print("Ничья!")
            break


# проверка выигрышных позиций, возвращает 'True' если игрок выиграл, 'False' если наоборот
def check_win(grid) :
    win_game_pos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for elem in win_game_pos : # elem: (0,1,2) etc.
        if grid[elem[0]] == grid[elem[1]] == grid[elem[2]] :
            return grid[elem[0]]
    return False


main(grid)
