"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_file = open(file_path)
    text_string = text_file.read().replace("\n", " ")

    text_file.close()

    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    word_list = text_string.split(" ")

    index = 0

    while index < (len(word_list) - 3):
        key = (word_list[index], word_list[index + 1])
        chains[key] = chains.get(key, [])
        new_list = chains.get(key)
        new_list.append(word_list[index + 2])
        chains[key] = new_list 
        index += 1
        #checker_string = str(key[0]) + " " + str(key[1])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    #Start with a random key from dictionary. Remember, this key is a tuple.
    chains_key = choice(list(chains))
    
    #Append the two words that compose the tuple to the list.
    words.append(str(chains_key[0]))
    words.append(str(chains_key[1]))
    
    #This while loop will run as long as the key is in the dictionary.
    while chains_key in chains.keys():
        
        #Get a random word from the list assigned to chains_key
        random_choice_from_key = choice(chains[chains_key])

        #Append that random word to the word list 
        words.append(random_choice_from_key)

        #Now, make a new chains key that is composed of the last two 
        #list items in the word list 
        chains_key = (words[-2], words[-1])

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
