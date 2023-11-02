import math 
def calculate_triangle_area(side):
    return (math.sqrt(3)/4)*side**2
len = float(input('Введите длину стороны шестиугольника:'))   
s = 6 * 
calculate_triangle_area(len)
print('Площадь правильного шестиугольника:',s)