# numbers.txt

# зчитування чисел з файлу та обчислення їх суми
with open("numbers.txt", "r") as f:
    numbers = f.readlines()
total = sum([int(x) for x in numbers])
# виведення суми на екран і запис до іншого файлу
print("Сума чисел:", total)
with open("sum_numbers.txt", "w") as f:
    f.write(str(total))