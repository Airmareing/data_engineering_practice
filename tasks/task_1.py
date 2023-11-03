from collections import Counter
import re


with open("../src_data/text_1_var_42", "r") as data:
    text = data.read()

words = re.findall(r'\w+', text.lower())
word_counts = Counter(words)
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

with open("../results/output_data_1.txt", "w") as output:
    for word, freq in sorted_word_counts:
        output.write(f"{word}:{freq}\n")