n = int(input("Введите число n: "))
s = 0
for i in range(1, n+1):
    s += i**3
print("Сумма:", s)
