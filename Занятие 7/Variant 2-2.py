array = []
positive_array = []
negative_array = []
N = int(input("Введите размер массива: "))
for i in range(N):
    num = int(input("Введите элемент массива: "))
    array.append(num)
for num in array:
    if num > 0:
        positive_array.append(num)
    else:
        negative_array.append(num)
print("Положительные элементы:", positive_array)
print("Отрицательные элементы:", negative_array)