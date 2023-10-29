N = int(input("Введите количество чисел из ряда Фибоначчи: "))
s = 0
a, b = 0, 1
for i in range(N):
    s += a
    a, b = b, a+b
print("Сумма чисел:", s)