n = int(input("Введите число n: "))
s = 0
factorial = 1
for i in range(1, n+1):
    factorial *= i
    s += factorial
print("Сумма факториалов:", s)