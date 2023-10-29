x = float(input("Введите начальное значение пробега x (в километрах): "))
y = float(input("Введите значение пробега y (в километрах): "))
day = 1
distance = x
while distance < y:
    distance += distance * 0.1
    day += 1
print("Номер дня:", day)