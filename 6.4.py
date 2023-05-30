# запитування імен та запис до файлу
with open("gu", "w") as f:
    while True:
        name = input("Введіть ваше ім'я (для виходу введіть quit): ")
        if name == "quit":
            break
    message = f"Вітаємо, {name}!\n"
    print(message)
    f.write(message)