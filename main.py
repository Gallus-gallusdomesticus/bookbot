from sys import *

if len(argv)==2:
    with open(argv[1]) as f:
        read_data=f.read()
else:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)



from stats import *

word_num=num_of_words(read_data)
alpha_count=alpha_list(read_data)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {word_num} total words")
print("--------- Character Count -------")
for diction in alpha_count:
    print(f"{diction["char"]}: {diction["count"]}")
print("============= END ===============")
