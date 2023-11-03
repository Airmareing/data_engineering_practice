import csv

average = 0
collumns = list()

with open("../src_data/text_4_var_42", newline='\n') as data:
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        item = {
            "number": int(row[0]),
            "name": row[2]+' '+row[1],
            "age": int(row[3]),
            "salary": int(row[4][0:-1])
        }

        average += item["salary"]
        collumns.append(item)

average /= len(collumns)

age_only = list()
for item in collumns:
    if (item["salary"] > average) and item["age"] > 27:
        age_only.append(item)

age_only = sorted(age_only, key=lambda i: i["number"])

print(age_only)

with open("../results/output_data_4.csv", 'w', newline='\n') as output:
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator=('₽'+"\n"))
    for item in age_only:
        writer.writerow(item.values())