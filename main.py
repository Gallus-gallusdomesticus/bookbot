with open("./books/frankenstein.txt") as f:
    read_data=f.read()


from stats import num_of_words

print(num_of_words(read_data))