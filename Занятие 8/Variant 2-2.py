def calculate_rectangle_area(dlin,shir):
    return dlin * shir
rectangle_areas = []
for i in range(3):
    dlin = float(input('Введите длину прямоугольника' + str(i+1) + ':'))
    shir = float(input('Введите ширину прямоугольника' + str(i+1) + ':'))
    s = calculate_rectangle_area(dlin,shir)
    rectangle_areas.append(s)
for i in range(3):
    print('Площадь прямоугольника',i+1,':',rectangle_areas[i])