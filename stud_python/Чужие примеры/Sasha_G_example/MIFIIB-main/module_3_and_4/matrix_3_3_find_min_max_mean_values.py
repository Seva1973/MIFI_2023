"""ПРИМЕР 3
Условие задачи: дана двумерная матрица 3 x 3. Определить максимум и минимум каждой строки, а также их индексы."""
N = 3
M = 3
random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]

mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

for row in random_matrix:  # здесь мы целиком берём каждую сроку
    min_index = 0  # в качестве минимального значения возьмём первый элемент строки
    max_index = 0
    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
    max_value = row[max_index]  # для максимального значения то же самое
    for index_col in range(len(row) ):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)

print("Матрица: ")
for i in range(N):
    for j in range(M):
        print(random_matrix[i][j], end='  ') # количество пробелов вставляемых между элементами строк матрицы
    print()  # перенос на новую строку

print("Минимальные значения для каждой строки матрицы: ", min_value_rows)
print("Индексы минимальных значений для каждой строки матрицы: ", min_index_rows)
print("Максимальные значения для каждой строки матрицы: ", max_value_rows)
print("Индексы максимальных значений для каждой строки матрицы: ", max_index_rows)
print("Расчёт минимальных и максимальных элементов матрицы осуществлён, до встречи!")