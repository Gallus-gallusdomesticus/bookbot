def num_of_words(text):
    num_words=0
    word_list=text.split()
    for word in word_list:
        num_words+=1
    return f"{num_words} words found in the document"

def num_each_alpha(text):
    text_lower=text.lower()
    word_list_lower=list(text_lower)
    word_set_lower=set(word_list_lower)
    word_dict={}
    for word_set in word_set_lower:
        num_word=0
        for word_list in word_list_lower:
            if word_set==word_list:
                num_word+=1
        word_dict[word_set]=num_word
    return word_dict

