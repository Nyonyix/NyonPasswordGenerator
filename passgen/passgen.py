import random
from datetime import datetime as dt

seed = dt.now()
word_file = "words.txt"
pass_file = "commonpass.txt"
symbol_list = "%^~|[]<>{}@#&*-+=()_$\"\'\:;/^"
num_list ="123456789"
#CONFIG - Default 2
num_of_words = 2

random.seed(seed)

def main():

    #CONFIG - Amount of passwords generated - Default 5
    for i in range(5):

        out = ''

        word_list = selectWords()

        #reselect words if words are common
        while(isCommon(word_list)):
            word_list = selectWords()

        word_list = scrambleWord(word_list)

        #reselects if the amount of words is less than expected.
        while(len(word_list) < num_of_words):
            word_list = selectWords()
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
    for i in range(num_of_words):
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

    final_list = [ ]
    scram_list = [ ]

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

        #builds new list of words with capitals for next section.
        scram_list.append(word.capitalize())

    #break each word into chars
    for word in scram_list:
        word_chars = list(word)

        #tries a random number each char, if below X, char becomes a capital.
        #CONFIG - Default 3
        for char in word_chars:
            if random.randint(0, 10) <= 3:
               rand_char_int = random.randint(0,len(word_chars)-1)
               word_chars[rand_char_int] = word_chars[rand_char_int].upper()

        #rebuilds word strings and appends to new output list.
        word_out = ''.join(word_chars)
        final_list.append(word_out)

    return final_list

def symbolGen():

    #defines the amount of symbols between words
    #CONFIG - Default 2,4
    rand_range = random.randint(2, 4)

    #shuffles the premade symbols string
    symbol_list_chars = list(symbol_list)
    random.shuffle(symbol_list_chars)

    #selects x first chars from the shuffled symbols string
    symbol_out = ''.join(symbol_list_chars[0:rand_range])

    return symbol_out

main()
