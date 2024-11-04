import tkinter as tk
from tkinter import messagebox

# Импортируем все необходимые функции из вашего файла
from matrix import add_matrices, multiply_matrices, transpose_matrix, scalar_multiply, determinant

# Функция для создания матрицы на основе пользовательского ввода
def create_matrix(entries, rows, cols):
    matrix = []
    try:
        for i in range(rows):
            row = [float(entries[i][j].get()) for j in range(cols)]
            matrix.append(row)
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный ввод. Все элементы матрицы должны быть числами.")
    return matrix

# Функция для отображения матрицы в текстовом формате и сообщения о выполненной операции
def display_matrix(matrix, label, operation_message):
    matrix_str = "\n".join(["\t".join(map(str, row)) for row in matrix])
    label.config(text=f"{operation_message}:\n{matrix_str}")

# Создание окна приложения
root = tk.Tk()
root.title("Матричные операции")

# Ввод размеров матриц
tk.Label(root, text="Количество строк первой матрицы:").grid(row=0, column=0)
rows1_entry = tk.Entry(root)
rows1_entry.grid(row=0, column=1)

tk.Label(root, text="Количество столбцов первой матрицы:").grid(row=1, column=0)
cols1_entry = tk.Entry(root)
cols1_entry.grid(row=1, column=1)

tk.Label(root, text="Количество строк второй матрицы:").grid(row=2, column=0)
rows2_entry = tk.Entry(root)
rows2_entry.grid(row=2, column=1)

tk.Label(root, text="Количество столбцов второй матрицы:").grid(row=3, column=0)
cols2_entry = tk.Entry(root)
cols2_entry.grid(row=3, column=1)

# Место для отображения введённых матриц
matrix1_frame = tk.Frame(root)
matrix2_frame = tk.Frame(root)

# Функция для динамического создания полей для ввода матриц
def setup_matrix_input():
    try:
        rows1 = int(rows1_entry.get())
        cols1 = int(cols1_entry.get())
        rows2 = int(rows2_entry.get())
        cols2 = int(cols2_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Количество строк и столбцов должно быть целым числом.")
        return

    # Очищаем старые поля ввода
    for widget in matrix1_frame.winfo_children():
        widget.destroy()
    for widget in matrix2_frame.winfo_children():
        widget.destroy()

    # Создание полей ввода для первой матрицы
    tk.Label(matrix1_frame, text="Первая матрица:").grid(row=0, column=0, columnspan=cols1)
    matrix1_entries = []
    for i in range(rows1):
        row_entries = []
        for j in range(cols1):
            entry = tk.Entry(matrix1_frame, width=5)
            entry.grid(row=i + 1, column=j)
            row_entries.append(entry)
        matrix1_entries.append(row_entries)

    matrix1_frame.grid(row=5, column=0, columnspan=2)

    # Создание полей ввода для второй матрицы
    tk.Label(matrix2_frame, text="Вторая матрица:").grid(row=0, column=0, columnspan=cols2)
    matrix2_entries = []
    for i in range(rows2):
        row_entries = []
        for j in range(cols2):
            entry = tk.Entry(matrix2_frame, width=5)
            entry.grid(row=i + 1, column=j)
            row_entries.append(entry)
        matrix2_entries.append(row_entries)

    matrix2_frame.grid(row=5, column=2, columnspan=2)

    # Кнопки для сложения и умножения матриц
    def execute_addition():
        matrix1 = create_matrix(matrix1_entries, rows1, cols1)
        matrix2 = create_matrix(matrix2_entries, rows2, cols2)
        result = add_matrices(matrix1, matrix2)
        if result:
            display_matrix(result, result_label, "Результат сложения матриц")

    def execute_multiplication():
        matrix1 = create_matrix(matrix1_entries, rows1, cols1)
        matrix2 = create_matrix(matrix2_entries, rows2, cols2)
        result = multiply_matrices(matrix1, matrix2)
        if result:
            display_matrix(result, result_label, "Результат умножения матриц")

    # Добавление кнопок для сложения и умножения матриц
    tk.Button(root, text="Сложение матриц", command=execute_addition).grid(row=7, column=0, columnspan=2)
    tk.Button(root, text="Умножение матриц", command=execute_multiplication).grid(row=7, column=2, columnspan=2)

    # Поля для ввода скаляра
    tk.Label(root, text="Введите скаляр первой матрицы:").grid(row=6, column=0)
    scalar_entry1 = tk.Entry(root)
    scalar_entry1.grid(row=6, column=1)

    tk.Label(root, text="Введите скаляр второй матрицы:").grid(row=6, column=2)
    scalar_entry2 = tk.Entry(root)
    scalar_entry2.grid(row=6, column=3)

    # Кнопки для операций с первой матрицей
    def execute_transpose_matrix1():
        matrix1 = create_matrix(matrix1_entries, rows1, cols1)
        result = transpose_matrix(matrix1)
        display_matrix(result, result_label, "Результат транспонирования первой матрицы")

    def execute_determinant_matrix1():
        matrix1 = create_matrix(matrix1_entries, rows1, cols1)
        result = determinant(matrix1)
        display_matrix([[result]], result_label, "Определитель первой матрицы")

    def execute_scalar_multiply_matrix1():
        matrix1 = create_matrix(matrix1_entries, rows1, cols1)
        scalar = float(scalar_entry1.get())
        result = scalar_multiply(matrix1, scalar)
        display_matrix(result, result_label, "Результат умножения первой матрицы на скаляр")

    # Кнопки для операций со второй матрицей
    def execute_transpose_matrix2():
        matrix2 = create_matrix(matrix2_entries, rows2, cols2)
        result = transpose_matrix(matrix2)
        display_matrix(result, result_label, "Результат транспонирования второй матрицы")

    def execute_determinant_matrix2():
        matrix2 = create_matrix(matrix2_entries, rows2, cols2)
        result = determinant(matrix2)
        display_matrix([[result]], result_label, "Определитель второй матрицы")

    def execute_scalar_multiply_matrix2():
        matrix2 = create_matrix(matrix2_entries, rows2, cols2)
        scalar = float(scalar_entry2.get())
        result = scalar_multiply(matrix2, scalar)
        display_matrix(result, result_label, "Результат умножения второй матрицы на скаляр")

    # Кнопки для транспонирования, определения и умножения на скаляр
    tk.Button(root, text="Транспонирование первой матрицы", command=execute_transpose_matrix1).grid(row=8, column=0)
    tk.Button(root, text="Определитель первой матрицы", command=execute_determinant_matrix1).grid(row=9, column=0)
    tk.Button(root, text="Умножение первой матрицы на скаляр", command=execute_scalar_multiply_matrix1).grid(row=10, column=0)

    tk.Button(root, text="Транспонирование второй матрицы", command=execute_transpose_matrix2).grid(row=8, column=2)
    tk.Button(root, text="Определитель второй матрицы", command=execute_determinant_matrix2).grid(row=9, column=2)
    tk.Button(root, text="Умножение второй матрицы на скаляр", command=execute_scalar_multiply_matrix2).grid(row=10, column=2)

# Кнопка для создания полей ввода матриц
tk.Button(root, text="Создать матрицы", command=setup_matrix_input).grid(row=4, column=0, columnspan=4)

# Место для отображения результата
result_label = tk.Label(root, text="")
result_label.grid(row=11, column=0, columnspan=4)

# Запуск основного цикла программы
root.mainloop()
