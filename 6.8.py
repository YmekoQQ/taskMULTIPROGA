# зчитування тексту з файлу
with open("MonteCristo.txt", "r") as f:
    text = f.read()
# розрахунок відсотків малих та великих літер
total_letters = len([char for char in text if char.isalpha()])
capital_letters = len([char for char in text if char.isalpha() and char.isupper()])
small_letters = len([char for char in text if char.isalpha() and char.islower()])
capital_percent = capital_letters / total_letters * 100
small_percent = small_letters / total_letters * 100
# виведення результатів
print(f"У тексті знаходиться: {capital_percent:.2f}% великих літер та {small_percent:.2f}% малих літер")