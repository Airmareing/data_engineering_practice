with open("../src_data/text_2_var_42", "r") as data:
    lines = data.readlines()

sumstr = []
for line in lines:
    numbers = line.split()
    total = 0
    for number in numbers:
        try:
            total += float(number)
        except ValueError:
            pass
    sumstr.append(total)

with open("../results/output_data_2.txt", "w") as output:
    for total in sumstr:
        output.write(f"{total}\n")
