# I want to figure out how many words are in this string
def word_count(s):
    words_seen_so_far = 0 # we're "accumulating" how many words we've seen
    current_state = "outside word"

    for c in s:
        is_this_a_space = c.isspace()
        if current_state == "outside word":
            if is_this_a_space:
                # stay where you are
                current_state = "outside word"
            else:
                current_state = "inside word"
                words_seen_so_far = words_seen_so_far + 1
        else: # I know I'm inside a word
            if is_this_a_space:
                current_state = "outside word"
            else:
                current_state = "inside word"

    return words_seen_so_far

