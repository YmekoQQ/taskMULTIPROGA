# зчитування тексту з файлу та обробка його рядків
with open("learning_python.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())  # strip() для видалення зайвих символів

# збереження рядків у списку та виведення списку поза блоком
with open("learning_python.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)