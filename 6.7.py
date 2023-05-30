# завантаження тексту книги import requests
import requests
url = "https://www.gutenberg.org/files/521/521-0.txt"
response = requests.get(url)
text = response.text
# знаходження заголовків розділів
chapters = []
for line in text.split("\n"):
    if line.startswith("CHAPTER "):
        chapters.append(line)
# збереження заголовків розділів у файл
with open("chapters.txt", "w") as f:
    for chapter in chapters:
        f.write(chapter + "\n")