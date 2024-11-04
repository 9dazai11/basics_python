import tkinter as tk
from tkinter import messagebox
import xmlrpc.client
import numpy as np

# Функция для генерации случайной матрицы
def generate_random_matrix(size):
    return np.random.randint(1, 100, size=(size, size))

# Функция для отображения матрицы в текстовом поле
def show_matrix(matrix, title):
    text_widget.insert(tk.END, f"{title}:\n" + "\n".join(["\t".join(map(str, row)) for row in matrix]) + "\n\n")

# Функции для вызова методов на сервере
def add_matrices():
    matrix_a = generate_random_matrix(3)
    matrix_b = generate_random_matrix(3)
    
    result = server.add_matrices(matrix_a.tolist(), matrix_b.tolist())
    
    text_widget.delete("1.0", tk.END)  # Очистка поля вывода перед каждым запуском операции
    show_matrix(matrix_a, "Матрица A")
    show_matrix(matrix_b, "Матрица B")
    show_matrix(result, "Результат сложения")

def multiply_matrices():
    matrix_a = generate_random_matrix(3)
    matrix_b = generate_random_matrix(3)
    
    result = server.multiply_matrices(matrix_a.tolist(), matrix_b.tolist())
    
    text_widget.delete("1.0", tk.END)
    show_matrix(matrix_a, "Матрица A")
    show_matrix(matrix_b, "Матрица B")
    show_matrix(result, "Результат умножения")

def transpose_matrix():
    matrix_a = generate_random_matrix(3)
    
    result = server.transpose_matrix(matrix_a.tolist())
    
    text_widget.delete("1.0", tk.END)
    show_matrix(matrix_a, "Исходная матрица")
    show_matrix(result, "Транспонированная матрица")

def determinant():
    matrix_a = generate_random_matrix(3)
    
    result = server.determinant(matrix_a.tolist())
    
    text_widget.delete("1.0", tk.END)
    show_matrix(matrix_a, "Исходная матрица")
    text_widget.insert(tk.END, f"Детерминант: {result}\n")

def compare_performance(operation):
    results = []
    
    if operation == "determinant":
        # Сравнение детерминанта только для матриц 10x10
        sizes = [10]
    else:
        sizes = [10, 50, 100]
    
    for size in sizes:
        matrix_a = generate_random_matrix(size)
        matrix_b = generate_random_matrix(size) if operation != "transpose" else None
        
        if operation == "add":
            c_time, py_time = server.compare_add_matrices(matrix_a.tolist(), matrix_b.tolist())
            operation_name = "Сложение матриц"
        elif operation == "multiply":
            c_time, py_time = server.compare_multiply_matrices(matrix_a.tolist(), matrix_b.tolist())
            operation_name = "Умножение матриц"
        elif operation == "transpose":
            c_time, py_time = server.compare_transpose_matrix(matrix_a.tolist())
            operation_name = "Транспонирование матрицы"
        elif operation == "determinant":
            c_time, py_time = server.compare_determinant(matrix_a.tolist())
            operation_name = "Вычисление детерминанта"
        
        results.append((size, py_time, c_time, operation_name))
    
    # Отображение результатов в текстовом поле
    text_widget.delete("1.0", tk.END)
    for size, py_time, c_time, operation_name in results:
        text_widget.insert(tk.END, f"{operation_name} для матрицы {size}x{size}:\n")
        text_widget.insert(tk.END, f"Выполнение функции на Python: {py_time:.6f} секунд\n")
        text_widget.insert(tk.END, f"Выполнение функции на C: {c_time:.6f} секунд\n\n")

# Подключаемся к серверу
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Создаем основное окно
root = tk.Tk()
root.title("Matrix Operations Client")

# Создаем текстовое поле для вывода результатов без автоматического переноса строк
text_widget = tk.Text(root, wrap="none", width=80, height=20)
text_widget.pack(pady=5)

# Создаем кнопки для операций
tk.Button(root, text="Сложить матрицы", command=add_matrices).pack(pady=5)
tk.Button(root, text="Умножить матрицы", command=multiply_matrices).pack(pady=5)
tk.Button(root, text="Транспонировать матрицу", command=transpose_matrix).pack(pady=5)
tk.Button(root, text="Вычислить детерминант", command=determinant).pack(pady=5)

# Кнопки для сравнения производительности
tk.Button(root, text="Сравнить производительность сложения", command=lambda: compare_performance("add")).pack(pady=5)
tk.Button(root, text="Сравнить производительность умножения", command=lambda: compare_performance("multiply")).pack(pady=5)
tk.Button(root, text="Сравнить производительность транспонирования", command=lambda: compare_performance("transpose")).pack(pady=5)
tk.Button(root, text="Сравнить производительность детерминанта", command=lambda: compare_performance("determinant")).pack(pady=5)

# Запускаем главный цикл
root.mainloop()
