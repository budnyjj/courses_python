usr_input = raw_input("Please, input some words in english: ")

words_upper = []
for word in usr_input.split(' '):
    if word.isupper():
        words_upper.append(word)

print 'Number of uppercase words:', len(words_upper)
print 'List of them:', words_upper
