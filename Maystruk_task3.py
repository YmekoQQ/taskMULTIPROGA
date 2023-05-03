# Multiparadigmatic  programming languages:Task_3
# Maystruk Sergey:IKM-221a
print('Multiparadigmatic  programming languages:Task_3\nMaystruk Sergey:IKM-221a')
import math

print("Майструк Сергій Леонідович")
print("Лабораторна работа номер 3 ")
x = float(input("Ввести число :"))
b = float(input("Ввести число :"))
n = math.sqrt(x-b)
u = math.tan(x)
y = (((n)/(2*b)) - n/b**2)
if y == 0:
    print ("Значення змінних виходять за область визначення функції")

elif y > 0 or y <0 :
    print("Відповідь :", y)