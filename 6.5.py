# список файлів для аналізу
files = ["book1.txt", "book2.txt", "book3.txt"]
# проходження по кожному файлу for file in files:
for file in files:
    with open(file, "r") as f:
        text = f.read()
    # підрахунок кількості входжень слова "the"
    count = text.lower().count("the")
    print(f"'the' зустрічається у файлі {files} {count} разів")