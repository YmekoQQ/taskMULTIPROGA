# завантаження тексту книги import requests
import requests

url = "https://www.gutenberg.org/files/1342/1342-0.txt"
response = requests.get(url)
text = response.text
# заміна розривів рядків на пробіли
formatted_text = text.replace("\n", " ")
# збереження відформатованого тексту у файл
with open("formatted_text.txt", "w") as f:
    f.write(formatted_text)