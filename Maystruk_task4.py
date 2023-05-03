# Multiparadigmatic  programming languages:Task_4
# Maystruk Sergey:IKM-221a
print('Multiparadigmatic  programming languages:Task_4\nMaystruk Sergey:IKM-221a')
n = int(input("Введіть кількість членів послідовності: "))

sum = 0
for i in range(n):
    sum += (2*i + 1)/(2*i + 2)

print("Сума перших", n, "членів послідовності дорівнює", sum)