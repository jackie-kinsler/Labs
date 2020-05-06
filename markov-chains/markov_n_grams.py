"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_file = open(file_path)
    text_string = text_file.read().replace("\n", " ")

    text_file.close()

    return text_string


def make_chains(text_string, chain_length):
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

    #The while loop whill continue until the end of the text. 
    #Adjustments are made to avoid index errors
    while index < (len(word_list) - (chain_length+1)):
        
        list_for_tuple = []
        
        #This for loop creates a list of length len(chain_length)
        for i in range(chain_length):
            list_for_tuple.append(word_list[index+i])
            #key = (word_list[index], word_list[index + 1])

        #Assign the key to be a tuple of the list created above
        key = tuple(list_for_tuple)
        chains[key] = chains.get(key, [])
        new_list = chains.get(key)
        new_list.append(word_list[index + (chain_length)])
        chains[key] = new_list 
        index += 1

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    #Start with a random key from dictionary. Remember, this key is a tuple.
    chains_key = choice(list(chains))
    
    #Append the words that compose the tuple to the list.
    for i in range(len(chains_key)):
        words.append(str(chains_key[i]))
    
    
    #This while loop will run as long as the key is in the dictionary.
    while chains_key in chains.keys():
        
        #Get a random word from the list assigned to chains_key
        random_choice_from_key = choice(chains[chains_key])
        
        #Append that random word to the word list 
        words.append(random_choice_from_key)
        # Now, make a new chains key that is composed of the last n 
        # list items in the word list 
        list_for_chains_key = []

        for i in range(len(chains_key)):
            list_item = words[i-len(chains_key)] 
            list_for_chains_key.append(list_item)
        
        chains_key = tuple(list_for_chains_key)

    return " ".join(words)

# def make_a_markov_chain_from_text():
#     print(make_text(make_chains(open_and_read_file(sys.argv[1]))))

# make_a_markov_chain_from_text()

input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text, 7)

# Produce random text
random_text = make_text(chains)

