def is_magic_square(matrix):
    n = len(matrix)
    target_sum = sum(matrix[0])
    for i in range(1, n):
        if sum(matrix[i]) != target_sum:
            return False
    for j in range(n):
        column_sum = 0
        for i in range(n):
            column_sum += matrix[i][j]
        if column_sum != target_sum:
            return False
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]
    if diagonal_sum != target_sum:
        return False
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][n - i - 1]
    if diagonal_sum != target_sum:
        return False
    return True

def read_matrix_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        matrix = [[int(num) for num in line.split()] for line in lines]
    return matrix

def write_result_to_file(file_name, result):
    with open(file_name, 'w') as file:
        file.write(result)

input_file_name = 'ФИО_группа_vvod.txt'
output_file_name = 'ФИО_группа_vivod.txt'

matrix = read_matrix_from_file(input_file_name)
result = "Magic square" if is_magic_square(matrix) else "Not a magic square"
write_result_to_file(output_file_name, result)