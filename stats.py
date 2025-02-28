def num_of_words(text):
    num_words=0
    word_list=text.split()
    for word in word_list:
        num_words+=1
    return f"{num_words} words found in the document"