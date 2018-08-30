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
        filtered_data = filtered_data + [word]

    # now, we need to keep track of the last two words, and remember to
    # predict the current word
    previous_previous_word = filtered_data[0]
    previous_word = filtered_data[1]
    for word in filtered_data[2:]:
        # remember the current word, and the last two word
        # save (previous_previous_word, previous_word) -> word in the dict

        if (previous_previous_word, previous_word) in predictions:
            # if we've seen this before, add to the current list of
            # predictions
            predictions[(previous_previous_word, previous_word)] = \
                predictions[(previous_previous_word, previous_word)] + \
                [word]
        else:
            # otherwise, we start a new index in this dictionary,
            # containing only [word]
            predictions[(previous_previous_word, previous_word)] = \
                [word]

if __name__ == '__main__':
    training_data = "The quick brown fox jumps over the quick brown dog."
    build_predictions_dict(training_data)
    print(predictions)