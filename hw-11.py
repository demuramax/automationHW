# The program has a string `sentences`.
# The string consists of sentences.
# A 'sentence' is a set of characters delimited by periods(. or ...) or the beginning of a line and a period.
# Return list with number of words in each sentence.
# A 'word' is a set of characters between two spaces or the beginning of a line and a space.
# DO NOT use regular expressions.

sentences = "Hello all. Here's pretty cold and hot. Choose yourself."
# words_number -> [2, 5, 2]

str_split = sentences.rsplit((' '))
words_number = []
counter = int()
for el in str_split:
    counter += 1
    if el.endswith('.') or el.endswith('...') is True:
        words_number.append(counter)
        counter = 0

print(words_number)