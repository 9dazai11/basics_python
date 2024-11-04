from xmlrpc.server import SimpleXMLRPCServer
from matrix import add_matrices, multiply_matrices, transpose_matrix, scalar_multiply, determinant

# Функции-обертки для добавления вывода в консоль
def add_matrices_wrapper(matrix1, matrix2):
    result = add_matrices(matrix1, matrix2)
    print(f"Выполнено сложение матриц:\n{matrix1}\n+\n{matrix2}\n=\n{result}")
    return result

def multiply_matrices_wrapper(matrix1, matrix2):
    result = multiply_matrices(matrix1, matrix2)
    print(f"Выполнено умножение матриц:\n{matrix1}\n*\n{matrix2}\n=\n{result}")
    return result

def transpose_matrix_wrapper(matrix):
    result = transpose_matrix(matrix)
    print(f"Выполнено транспонирование матрицы:\n{matrix}\n=\n{result}")
    return result

def scalar_multiply_wrapper(matrix, scalar):
    result = scalar_multiply(matrix, scalar)
    print(f"Выполнено умножение матрицы на скаляр:\n{matrix}\n*\n{scalar}\n=\n{result}")
    return result

def determinant_wrapper(matrix):
    result = determinant(matrix)
    print(f"Выполнено нахождение определителя матрицы:\n{matrix}\n=\n{result}")
    return result

# Создаем сервер
server = SimpleXMLRPCServer(("localhost", 8000))
print("Сервер запущен и ожидает запросы...")

# Регистрируем функции, которые будут доступны клиенту
server.register_function(add_matrices_wrapper, "add_matrices")
server.register_function(multiply_matrices_wrapper, "multiply_matrices")
server.register_function(transpose_matrix_wrapper, "transpose_matrix")
server.register_function(scalar_multiply_wrapper, "scalar_multiply")
server.register_function(determinant_wrapper, "determinant")

# Запускаем сервер
server.serve_forever()
