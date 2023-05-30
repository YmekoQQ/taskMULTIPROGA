# зчитування тексту з файлу та заміна слова Python на C
with open("learning_python.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    print(line.replace("Python", "C").strip()) # заміна та видалення зайвих символів