import random
from datetime import datetime as dt

seed = dt.now()
word_file = "words.txt"
pass_file = "commonpass.txt"
num_symbol = "%^~|[]<>{}@#&*-+=()_$\"\'\:;/^1234567890"

random.seed(seed)

def main():

    for i in range(40):

        out = ''

        word_list = selectWords()

        #reselect words if words are common
        while(isCommon(word_list)):
            word_list = selectWords()

        word_list = scrambleWord(word_list)

        #reselects if the amount of words is less than expected.
        while(len(word_list) < 1):
            word_list = createWordList()
            word_list = scrambleWord(word_list)

        #builds final string
        for word in word_list:
            out += word + symbolGen()

        print(out)

def selectWords():

    #imports and cleans the list of words.
    with open(word_file, 'r') as f_words:
        raw_word_list = f_words.readlines()
        raw_word_list = [s.strip('\n') for s in raw_word_list]
        word_list = filter(lambda raw_words: len(raw_words) >= 6, raw_word_list)
        word_list = list(word_list)

    #randomly selects x amount of words.
    out_list = []
    for i in range(2):
        random_int = random.randint(0, (len(word_list)-1))
        out_list.append(word_list[random_int])

        f_words.close()

    return out_list

def isCommon(word_list):

    #open and cleans the list of commons passwords.
    with open(pass_file, 'r') as f_pass:
        pass_list = f_pass.readlines()
        pass_list = [s.strip('\n') for s in pass_list]

    #checks if the selected words are common passwords.
    is_common = False
    for word in word_list:
        if word in pass_list:
            is_common = True

    return is_common

def scrambleWord(word_list):

    new_list = [ ]

    for word in word_list:

        #a catch if the word is odd numbered in length.
        if (len(word) % 2) is not 0:
            half = (len(word) + 1) / 2

        #breaks the word into 3 parts based on the center.
        half = int(len(word) / 2)
        half_min, half_add = half - 1, half + 2
        start, mid, end = word[0:half_min], word[half_min:half_add], word[half_add:len(word)]

        #shuffles middle characters
        mid_chars = list(mid)
        random.shuffle(mid_chars)

        #reconstructs word
        mid = ''.join(mid_chars)
        word = start + mid + end

        #builds new list for words
        new_list.append(word)

    return new_list

def symbolGen():

    #defines the amount of symbols between words
    rand_range = random.randint(1, 3)

    #shuffles the premade symbols string
    num_symbol_chars = list(num_symbol)
    random.shuffle(num_symbol_chars)

    #selects x first chars from the shuffled symbols string
    symbol_out = ''.join(num_symbol_chars[0:rand_range])

    return symbol_out

main()
