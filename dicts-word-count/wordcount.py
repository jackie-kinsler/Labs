
import sys

def make_word_counts():
    
    wordcount_in_textfile = {}

    #Write a table that takes ASCII values and translates them to other characters
    #In this case, the other character is None
    #Table handles: .(46) ,(44) !(33) ?(63) ;(59) :(58) _(95) "(34)
    punctuation = { 44 : None, 46 : None, 33 : None, 63 : None, 59 : None, 
                    58 : None, 95 : None, 34 : None}

    textfile = open(sys.argv[1])

    for line in textfile:
        words = line.rstrip().split(" ")  #check if .strip() works better!
        for word in words:
            word_without_punctuation = word.translate(punctuation).lower()
            wordcount_in_textfile[word_without_punctuation] = wordcount_in_textfile.get(word_without_punctuation, 0) + 1

    for word_pair in wordcount_in_textfile.items():
        print(word_pair[0], word_pair[1])

    textfile.close

make_word_counts()



