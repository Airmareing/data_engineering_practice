import requests
from bs4 import BeautifulSoup
import csv

with open("../src_data/text_5_var_42", "r", encoding="utf-8") as data:
    html = data.read()

soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")
data_list = []

for row in table.find_all("tr"):
    cols = row.find_all("td")
    if cols:
        data_row = [col.text.strip() for col in cols]
        data_list.append(data_row)

with open("../results/output_data_5.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data_list)