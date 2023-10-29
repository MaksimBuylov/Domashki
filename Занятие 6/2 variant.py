string = input("Введите строку: ")
count = 0
new_string = ""
for i in string:
    if i == ":":
        new_string += "%"
        count += 1
    else:
        new_string += i
print("Измененная строка:", new_string)
print("Количество замен:", count)