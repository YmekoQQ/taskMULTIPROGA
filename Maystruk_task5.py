import math

tolerance = 1e-4
n = 1
sum = 0

while True:
    # обчислюємо загальний член ряду з формули Стірлінга
    an = 10 ** (-n) * math.sqrt(2 * math.pi * n) * ((n / math.e) ** (n - 1))

    sum += an

    # перевіряємо, чи досягнута потрібна точність
    if an < tolerance:
        break

    n += 1

print("Сума ряду з точністю", tolerance, "дорівнює", sum)