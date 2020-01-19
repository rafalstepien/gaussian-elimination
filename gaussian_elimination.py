#!bin/python3

# 1. Concatenate column vector with coefficients matrix to get one array
# 2. Transform array to upper-triangle matrix (zeros under diagonal)
# 3. Make zeros of upper-diagonal part of triangle matrix
import numpy as np


def create_upper_triangle(coefficients_matrix, column_vector):
	working_matrix = np.concatenate((coefficients_matrix, column_vector), axis=1)
	# macierz robocza ma jedna wiecej kolumne, bo dodalismy do niej wektor wyrazow wolnych, np. (3, 4)
	for i in range(working_matrix.shape[1]):  # iteracja po kolumnach
		for j in range(working_matrix.shape[0]):  # iteracja po wierszach
			if i == j and working_matrix[i][i] != 1 and working_matrix[i][i] != 0:
				working_matrix[i] = np.divide(working_matrix[i], working_matrix[i][i])
			if j > i:
				working_matrix[j] = working_matrix[j] - working_matrix[j][i] * working_matrix[i]
	return working_matrix

def zero_upper_triangle(upper_triangle_matrix):
	for i in range(upper_triangle_matrix.shape[1]-2, -1, -1):  # column
		for j in range(upper_triangle_matrix.shape[0]-1, -1, -1):  # row
			if i > j:
				upper_triangle_matrix[j] = upper_triangle_matrix[j] - upper_triangle_matrix[j][i] * upper_triangle_matrix[i]
	return upper_triangle_matrix

def gaussian_elimination(coefficients_matrix, column_vector):
	upper_triangle_matrix = create_upper_triangle(coefficients_matrix, column_vector)
	result_matrix = zero_upper_triangle(upper_triangle_matrix)
	return result_matrix[:, coefficients_matrix.shape[1]]

if __name__ == "__main__":
	print(gaussian_elimination(coefficients_matrix, column_vector))
