#include <stdlib.h>
#include "matrix.h"

// Функция для выделения памяти под матрицу размером rows x cols
int **allocate_matrix(int rows, int cols) {
    int **matrix = malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++) {
        matrix[i] = malloc(cols * sizeof(int));
    }
    return matrix;
}

// Функция для освобождения памяти матрицы
void free_matrix(int **matrix, int rows) {
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

// Сложение матриц
void add_matrices(int **matrix_a, int **matrix_b, int rows, int cols, int **result) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = matrix_a[i][j] + matrix_b[i][j];
        }
    }
}

// Умножение матриц
void multiply_matrices(int **matrix_a, int rows_a, int cols_a, int **matrix_b, int cols_b, int **result) {
    for (int i = 0; i < rows_a; i++) {
        for (int j = 0; j < cols_b; j++) {
            result[i][j] = 0;
            for (int k = 0; k < cols_a; k++) {
                result[i][j] += matrix_a[i][k] * matrix_b[k][j];
            }
        }
    }
}

// Транспонирование матрицы
void transpose_matrix(int **matrix, int rows, int cols, int **result) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[j][i] = matrix[i][j];
        }
    }
}

// Вычисление детерминанта матрицы
int determinant(int **matrix, int n) {
    if (n == 1) {
        return matrix[0][0];
    }

    if (n == 2) {
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
    }

    int det = 0;
    for (int c = 0; c < n; c++) {
        int **minor = allocate_matrix(n - 1, n - 1);
        for (int i = 1; i < n; i++) {
            int minor_col = 0;
            for (int j = 0; j < n; j++) {
                if (j != c) {
                    minor[i - 1][minor_col] = matrix[i][j];
                    minor_col++;
                }
            }
        }

        det += (c % 2 == 0 ? 1 : -1) * matrix[0][c] * determinant(minor, n - 1);
        free_matrix(minor, n - 1);
    }

    return det;
}