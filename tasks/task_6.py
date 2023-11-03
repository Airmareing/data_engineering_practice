import requests

API_KEY = "5a26c39d3c8eb5016509808939bf0071"

city = "Moscow"
country = "RU"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}"
response = requests.get(url)
data = response.json()
print(data)

# изначально задумка была в выводе актуальной погоды, но сервис выдаёт ошибку неактульного Key API, поэтому
# я принял решение построиться под обстоятельства (возможно ключ ещё не активирован и это произойдёт через какое-то время)
code = data["cod"]
message = data["message"]

html = f"<h1>Погода в {city}, {country}</h1>"
html += f"<p>Ошибка: {code}</p>"
html += f"<p>Описание: {message}</p>"

with open("../results/output_data_6.html", "w", encoding="utf-8") as output:
    output.write(html)