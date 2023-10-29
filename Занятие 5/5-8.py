sequence = []
num = int(input("Введите число: "))
max_count = 0
current_count = 1
while num != 0:
    sequence.append(num)
    if len(sequence) > 1:
        if num == sequence[-2]:
            current_count += 1
        else:
            current_count = 1
        if current_count > max_count:
            max_count = current_count
    num = int(input("Введите число: "))
print("Наибольшее количество подряд идущих равных элементов:", max_count)