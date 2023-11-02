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