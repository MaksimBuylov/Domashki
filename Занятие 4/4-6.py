n = int(input("Введите число n: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print("Факториал числа", n, "равен", factorial)
