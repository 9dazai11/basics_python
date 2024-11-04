# Создание двух матриц
def create_matrices(num_matrices=2):

    matrices = []
    
    for matrix_num in range(1, num_matrices + 1):
        # Ввод размеров матрицы
        rows = int(input(f"Введите количество строк для матрицы {matrix_num}: "))
        cols = int(input(f"Введите количество столбцов для матрицы {matrix_num}: "))

        matrix = []

        # Ввод элементов матрицы
        print(f"Введите элементы матрицы {matrix_num} построчно:")
        for i in range(rows):
            row = []
            for j in range(cols):
                element = float(input(f"Элемент [{i+1}][{j+1}]: "))
                row.append(element)
            matrix.append(row)

        matrices.append(matrix)

    return matrices

# Сложение матриц
def add_matrices(matrix1, matrix2):
    # Проверка совместимости для сложения
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Ошибка: Матрицы должны быть квадратными.")
        return None

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

# Умножение матриц
def multiply_matrices(matrix1, matrix2):
    # Проверка совместимости для умножения
    if len(matrix1[0]) != len(matrix2):
        print("Ошибка: Количество столбцов первой матрицы должно совпадать с количеством строк второй.")
        return None

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

#Транспонирование матрицы
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result =[]
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result

# Умножение матрицы на скаляр
def scalar_multiply(matrix, scalar):
    result = []
    for row in matrix:
        new_row = [element * scalar for element in row]
        result.append(new_row)
    return result

# Нахождение определителя матрицы
def determinant(matrix):
    # Проверка, является ли матрица квадратной
    if len(matrix) != len(matrix[0]):
        print("Ошибка: Определитель можно вычислить только для квадратных матриц.")
        return None

    # Базовый случай для 2x2 матрицы
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        minor = [row[:c] + row[c + 1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
    return det

# matrix1, matrix2 = create_matrices()
# # Вывод матриц
# print("Матрица 1:")
# for row in matrix1:
#     print(row)

# print("Матрица 2:")
# for row in matrix2:
#     print(row)

# # Сложение матриц
# print("Результат сложения матриц:")
# result_add = add_matrices(matrix1, matrix2)
# if result_add:
#     for row in result_add:
#         print(row)

# # Умножение матриц
# print("Результат умножения матриц:")
# result_multiply = multiply_matrices(matrix1, matrix2)
# if result_multiply:
#     for row in result_multiply:
#         print(row)

# # Вывод транспонирования матриц
# print("Транспонированная первая матрица:")
# transposed_matrix1 = transpose_matrix(matrix1)
# for row in transposed_matrix1:
#     print(row)

# print("Транспонированная вторая матрица:")
# transposed_matrix2 = transpose_matrix(matrix2)
# for row in transposed_matrix2:
#     print(row)

# # Умножение на скаляр
# scalar1 = float(input("Введите скаляр для умножения первой матрицы: "))
# result_scalar1 = scalar_multiply(matrix1, scalar1)
# print(f"Результат умножения первой матрицы на {scalar1}:")
# for row in result_scalar1:
#     print(row)

# scalar2 = float(input("Введите скаляр для умножения второй матрицы: "))
# result_scalar2 = scalar_multiply(matrix2, scalar2)
# print(f"Результат умножения второй матрицы на {scalar2}:")
# for row in result_scalar2:
#     print(row)

# # Нахождение определителя
# print("Определитель первой матрицы:")
# result_det1 = determinant(matrix1)
# if result_det1 is not None:
#     print(result_det1)

# print("Определитель второй матрицы:")
# result_det2 = determinant(matrix2)
# if result_det2 is not None:
#     print(result_det2)