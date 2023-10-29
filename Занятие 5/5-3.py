N = int(input("Введите натуральное число N: "))
power = 0
result = 1
while result * 2 <= N:
    result *= 2
    power += 1
print("Показатель степени:", power)
print("Степень:", result)