def swap_columns(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        matrix[i][0], matrix[i][m-1] = matrix[i][m-1], matrix[i][0]

    with open('ФИО_группа_vvod.txt', 'r') as file:
        lines = file.readlines()
        matrix = [[int(num) for num in line.split()] for line in lines]

    for row in matrix:
        print(row)

    with open('ФИО_группа_vivod.txt', 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')