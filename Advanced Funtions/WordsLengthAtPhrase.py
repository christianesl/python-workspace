my_string = "How long are the words in this phrase"
list(map(lambda x : len(x), my_string.split(" ")))

output: 3,4,3,3,5,2,4,6


solution:
def word_lengths(phrase):
    return list(map(len, phrase.split()))