import random

# I want to predict the next word to type
# based on the previous words that I've seen

# For example, if all I've ever seen is "The quick brown fox",
# I want to suggest "brown" every time you type "The quick"

# So we're remembering the last two words typed, and then making
# a suggestion based on that

# this dictionary will have as keys tuples of two words
# the values will be lists of the next word we see
# e.g., we want this to look something like:
# {('the', 'quick'): ['brown'], ('quick', 'brown'): ['fox', 'dog']}
# if the string was "The quick brown fox jumps over quick brown dog."
predictions = {}

# convert word to lowercase and remove punctuation
def filter_word(word):
    word = word.lower() # word is now lowercase

    word_without_punctuation = ""
    for character in word:
        # so, if word was "the", character would be 't', then 'h', then 'e'
        if character.isalnum():
            # remember this character, because it's not punctuation
            word_without_punctuation = word_without_punctuation + character

    return word_without_punctuation

def build_predictions_dict(training_data):
    # training_data is a string
    # get all the words first:
    training_data = training_data.split()
    # training data is a list of words
    # now, let's make all the words lowercase and get rid of punctuation
    filtered_data = []
    for word in training_data:
        # now I'm working on an individual word
        word = filter_word(word)
        filtered_data.append(word) # filtered_data = filtered_data + [word] took too long

    # now, we need to keep track of the last two words, and remember to
    # predict the current word
    last_last_word = filtered_data[0]
    last_word = filtered_data[1]
    for word in filtered_data[2:]:
        # remember the current word, and the last two word
        # save (last_last_word, last_word) -> word in the dict

        if (last_last_word, last_word) in predictions:
            # if we've seen this before, add to the current list of
            # predictions
            predictions[(last_last_word, last_word)] = \
                predictions[(last_last_word, last_word)] + \
                [word]
        else:
            # otherwise, we start a new index in this dictionary,
            # containing only [word]
            predictions[(last_last_word, last_word)] = \
                [word]

        # I'm done adding to the predictions dict now
        # let's advance last_last_word and last_word
        last_last_word = last_word
        last_word = word

def predict(last_last_word, last_word):
    # let's predict based on the training data a word
    # from the predictions dictionary. And we should randomly
    # choose one of the options for this
    # (last_last_word, last_word) pair
    options = predictions[(last_last_word, last_word)]
    # options is a list of strings to choose from
    # let's choose randomly out of options now
    return random.choice(options)

def generate_string(length, starting_word_1, starting_word_2):
    # to generate a string based on the training data we've seen,
    # we need to first pick two starting words
    # we can do this by getting a random key out of the dictionary

    # if starting_word_1, starting_word_2 are empty,
    # pick a random key like before for the starting words

    if starting_word_1 == "" and starting_word_2 == "":
        random_key = random.choice(list(predictions.keys()))
        last_last_word = random_key[0]
        last_word = random_key[1]
    else:
        last_last_word = starting_word_1
        last_word = starting_word_2

    # we've already predicted two words!
    length = length - 2

    result = last_last_word + " " + last_word

    # then, we can use the predict function until we reach len words
    # OR we don't have anything to predict
    for i in range(length): # iterate "length" times
        # predict a word ONLY IF (last_last_word, last_word) is in the 
        # predictions dictionary
        if (last_last_word, last_word) in predictions:
            next_word = predict(last_last_word, last_word)
            # update last_last_word and last_word
            last_last_word = last_word
            last_word = next_word
            # add the next_word to our result
            result += " " + next_word
        else:
            # stop the loop
            break

    # return our final result of length at most length
    return result

if __name__ == '__main__':
    in_file = open("../shakespeare.txt")
    training_data = in_file.read()
    in_file.close()
    #training_data = "The quick brown fox jumps over the quick brown dog."
    build_predictions_dict(training_data)
    #print(predictions)

    #print(predict("quick", "brown"))

    # let's ask the user how long they want the string to be
    length = int(input("Enter how long you want your string: "))
    # and ask for two starting words
    starting_words = input("Optionally, enter two starting words: ").split()
    if len(starting_words) == 2:
        starting_word_1 = starting_words[0]
        starting_word_2 = starting_words[1]
    else:
        starting_word_1 = ""
        starting_word_2 = ""
    # (and if they don't give any, let's just pick randomly)
    print(generate_string(length, starting_word_1, starting_word_2))