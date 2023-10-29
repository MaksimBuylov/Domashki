N = int(input("Введите количество чисел из ряда Фибоначчи: "))
K = int(input("Введите порядковый номер: "))
s = 0
a, b = 0, 1
for i in range(K):
    if i >= N:
        break
    s += a
    a, b = b, a+b
print("Сумма чисел:", s)