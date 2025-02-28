with open("./books/frankenstein.txt") as f:
    read_data=f.read()


from stats import num_each_alpha

print(num_each_alpha(read_data))