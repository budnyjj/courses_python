infile = open('input.txt', 'r')
words = infile.read().split()
infile.close()

counts = {}
for w in words:
    counts[w] = counts.get(w,0) + 1

outfile = open('output.txt', 'w')
for w in sorted(counts, key=counts.get, reverse=True):
    outfile.write("| {:20} | {} time(s) |\n".format(w, counts[w]))
outfile.close()
