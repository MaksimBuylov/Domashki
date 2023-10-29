array = []
N = int(input("Введите размер массива: "))
for i in range(N):
    num = int(input("Введите элемент массива: "))
    array.append(num)
min_element = array[0]
min_index = 0
for i in range(1, N):
    if array[i] < min_element:
        min_element = array[i]
        min_index = i
print("Минимальный элемент:", min_element)
print("Индекс минимального элемента:", min_index)