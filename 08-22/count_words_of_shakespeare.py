import word_count

# word_count.word_count(s)

if __name__ == "__main__":
    file = open("../shakespeare.txt")
    file_as_string = file.read()
    file.close()

    number_of_words = word_count.word_count(file_as_string)

    print("The number of words is", number_of_words)
