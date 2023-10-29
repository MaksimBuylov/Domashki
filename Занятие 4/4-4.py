N = int(input("Введите количество чисел: "))
s = 0
for i in range(N):
    num = int(input("Введите число: "))
    s += num
print("Сумма чисел:", s)