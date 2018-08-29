# we want to create a dictionary with keys as words and values
# as the number of times that word is used

# we start with the empty dict
# keys will be strings (words)
# values will be ints (counts)
word_count = {}

shakespeare_file = open("../shakespeare.txt")
words = shakespeare_file.read()
# right now, words is just a very long string;
# we need to separate out the words
words = words.split()
# now, words is a list of all the words

# now, go through all the words and count them
for word in words:
    # word is a string that represents one of the words in the file
    # either word has already been counted once, or it doesn't exist
    # in the word_count dictionary

    # let's make the word lowercase
    word = word.lower()

    # let's get rid of puncutation
    # get rid of punctuation if it's the last character
    if not word[-1].isalpha():
        # now we know the last character is not a-z
        # get rid of it
        word = word[0:-1]

    if len(word) == 0:
        continue # don't consider empty words

    # do the same thing if there's some non-alphabetic character
    # at the start of the word
    if not word[0].isalpha():
        # now we know the last character is not a-z
        # get rid of it
        word = word[1:]
    
    if word in word_count:
        # I've seen this word before
        old_count = word_count[word]
        word_count[word] = old_count + 1
    else:
        word_count[word] = 1

print(word_count)

# let's find the word that occurs the most
word_that_occurs_the_most = ""
count_for_that_word = -1
for (word, count) in word_count.items():
    # .items() goes through the dictionary and gives back
    # (key, value) pairs
    if count > count_for_that_word:
        # replace word_that_occurs_the_most with word
        word_that_occurs_the_most = word
        count_for_that_word = count

print("{} occurs the most with a count of {}".format(word_that_occurs_the_most,
                                                     count_for_that_word))
