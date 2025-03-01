with open("./books/frankenstein.txt") as f:
    read_data=f.read()


from stats import *

frank_word_num=num_of_words(read_data)
frank_alpha_count=alpha_list(read_data)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {frank_word_num} total words")
print("--------- Character Count -------")
for diction in frank_alpha_count:
    print(f"{diction["alpha"]}: {diction["num"]}")
print("============= END ===============")
        