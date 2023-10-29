sequence = []
num = int(input("Введите число: "))
count = 0
while num != 0:
    sequence.append(num)
    if len(sequence) > 1 and num > sequence[-2]:
        count += 1
    num = int(input("Введите число: "))
print("Количество элементов, больших предыдущего:", count)
