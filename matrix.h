#ifndef MATRIX_H
#define MATRIX_H

// Функция для выделения памяти под матрицу размером rows x cols
int **allocate_matrix(int rows, int cols);

// Функция для освобождения памяти матрицы
void free_matrix(int **matrix, int rows);

// Сложение матриц
void add_matrices(int **matrix_a, int **matrix_b, int rows, int cols, int **result);

// Умножение матриц
void multiply_matrices(int **matrix_a, int rows_a, int cols_a, int **matrix_b, int cols_b, int **result);

// Транспонирование матрицы
void transpose_matrix(int **matrix, int rows, int cols, int **result);

// Вычисление детерминанта матрицы
int determinant(int **matrix, int n);

#endif