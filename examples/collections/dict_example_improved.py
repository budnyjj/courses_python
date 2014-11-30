from collections import Counter

with open('input.txt', 'r') as infile:
    words = infile.read().split()

counts = Counter(words)

with open('output.txt', 'w') as outfile:
    for w,n in counts.most_common():
        outfile.write("| {:20} | {} time(s) |\n".format(
                      w, n))
