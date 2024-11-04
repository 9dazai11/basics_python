from xmlrpc.server import SimpleXMLRPCServer
import matrix
import ctypes
import numpy as np
import time

lib = ctypes.CDLL('./matrix.dll')

# Определение типов аргументов и возвращаемых значений для каждой функции
lib.add_matrices.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_int)),
                             ctypes.POINTER(ctypes.POINTER(ctypes.c_int)),
                             ctypes.c_int, ctypes.c_int,
                             ctypes.POINTER(ctypes.POINTER(ctypes.c_int))]

lib.multiply_matrices.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_int)),
                                  ctypes.c_int, ctypes.c_int,
                                  ctypes.POINTER(ctypes.POINTER(ctypes.c_int)),
                                  ctypes.c_int,
                                  ctypes.POINTER(ctypes.POINTER(ctypes.c_int))]

lib.transpose_matrix.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_int)),
                                 ctypes.c_int, ctypes.c_int,
                                 ctypes.POINTER(ctypes.POINTER(ctypes.c_int))]

lib.determinant.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_int)), ctypes.c_int]
lib.determinant.restype = ctypes.c_int

# Вспомогательные функции для конвертации numpy-матриц в формат C
def numpy_to_c_matrix(np_matrix):
    rows, cols = np_matrix.shape
    matrix_type = ctypes.POINTER(ctypes.c_int) * rows
    c_matrix = matrix_type()
    for i in range(rows):
        row_type = ctypes.c_int * cols
        c_row = row_type(*np_matrix[i])
        c_matrix[i] = ctypes.cast(c_row, ctypes.POINTER(ctypes.c_int))
    return c_matrix

def c_matrix_to_numpy(c_matrix, rows, cols):
    return np.array([[c_matrix[i][j] for j in range(cols)] for i in range(rows)])

# Функции для вызова методов на C
def add_matrices_c(matrix_a, matrix_b):
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)
    rows, cols = matrix_a.shape
    c_matrix_a = numpy_to_c_matrix(matrix_a)
    c_matrix_b = numpy_to_c_matrix(matrix_b)
    result_matrix = (ctypes.POINTER(ctypes.c_int) * rows)()
    for i in range(rows):
        result_matrix[i] = (ctypes.c_int * cols)()

    lib.add_matrices(c_matrix_a, c_matrix_b, rows, cols, result_matrix)
    return c_matrix_to_numpy(result_matrix, rows, cols).tolist()

def multiply_matrices_c(matrix_a, matrix_b):
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)
    rows_a, cols_a = matrix_a.shape
    rows_b, cols_b = matrix_b.shape
    c_matrix_a = numpy_to_c_matrix(matrix_a)
    c_matrix_b = numpy_to_c_matrix(matrix_b)
    result_matrix = (ctypes.POINTER(ctypes.c_int) * rows_a)()
    for i in range(rows_a):
        result_matrix[i] = (ctypes.c_int * cols_b)()

    lib.multiply_matrices(c_matrix_a, rows_a, cols_a, c_matrix_b, cols_b, result_matrix)
    return c_matrix_to_numpy(result_matrix, rows_a, cols_b).tolist()

def transpose_matrix_c(matrix):
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    c_matrix = numpy_to_c_matrix(matrix)
    result_matrix = (ctypes.POINTER(ctypes.c_int) * cols)()
    for i in range(cols):
        result_matrix[i] = (ctypes.c_int * rows)()

    lib.transpose_matrix(c_matrix, rows, cols, result_matrix)
    return c_matrix_to_numpy(result_matrix, cols, rows).tolist()

def determinant_c(matrix):
    matrix = np.array(matrix)
    n = matrix.shape[0]
    c_matrix = numpy_to_c_matrix(matrix)
    return int(lib.determinant(c_matrix, n))

#Функции для сравнения времени выполнения
def compare_add_matrices(matrix_a, matrix_b):
    start_c = time.time()
    add_matrices_c(matrix_a, matrix_b)
    end_c = time.time()

    start_py = time.time()
    matrix.add_matrices(matrix_a, matrix_b)
    end_py = time.time()

    return end_c - start_c, end_py - start_py

def compare_multiply_matrices(matrix_a, matrix_b):
    start_c = time.time()
    multiply_matrices_c(matrix_a, matrix_b)
    end_c = time.time()

    start_py = time.time()
    matrix.multiply_matrices(matrix_a, matrix_b)
    end_py = time.time()

    return end_c - start_c, end_py - start_py

def compare_transpose_matrix(matrix_a):
    start_c = time.time()
    transpose_matrix_c(matrix_a)
    end_c = time.time()

    start_py = time.time()
    matrix.transpose_matrix(matrix_a)
    end_py = time.time()

    return end_c - start_c, end_py - start_py

def compare_determinant(matrix_a):
    start_c = time.time()
    determinant_c(matrix_a)
    end_c = time.time()

    start_py = time.time()
    matrix.determinant(matrix_a)
    end_py = time.time()

    return end_c - start_c, end_py - start_py

# Создаем сервер
server = SimpleXMLRPCServer(("localhost", 8000))
print("Сервер запущен и ожидает запросы...")

# Регистрируем функции, которые будут доступны клиенту
server.register_function(add_matrices_c, "add_matrices")
server.register_function(multiply_matrices_c, "multiply_matrices")
server.register_function(transpose_matrix_c, "transpose_matrix")
server.register_function(determinant_c, "determinant")

#Регистрация функций для сравнения времени выполнения
server.register_function(compare_add_matrices, "compare_add_matrices")
server.register_function(compare_multiply_matrices, "compare_multiply_matrices")
server.register_function(compare_transpose_matrix, "compare_transpose_matrix")
server.register_function(compare_determinant, "compare_determinant")

# Запускаем сервер
server.serve_forever()