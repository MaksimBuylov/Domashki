sequence = []
num = int(input("Введите число: "))
while num != 0:
    sequence.append(num)
    num = int(input("Введите число: "))
average = sum(sequence) / len(sequence)
print("Среднее значение:", average)