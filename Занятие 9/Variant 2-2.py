def swap_columns(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        matrix[i][0], matrix[i][m-1] = matrix[i][m-1], matrix[i][0]
        
    for row in matrix:
        print(row)