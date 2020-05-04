
def make_word_counts(textfile):
    
    wordcount_in_textfile = {}

    textfile = open(textfile)

    for line in textfile:
        words = line.rstrip().split(" ")
        for word in words:
            wordcount_in_textfile[word] = wordcount_in_textfile.get(word, 0) +1

    textfile.close

    return wordcount_in_textfile

print(make_word_counts("test.txt"))
