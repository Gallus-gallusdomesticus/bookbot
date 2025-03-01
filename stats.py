#FUNCTION TO COUNT HOW MANY WORDS TOTAL IN THE BOOK
def num_of_words(text):
    num_words=0
    word_list=text.split()
    for word in word_list:
        num_words+=1
    return num_words

#FUNCTION TO COUNT HOW MANY EACH LETTER AND SYMBOL IN A BOOK
#complicated method (mine)
def num_each(text):
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

#simple method
def num_each_simple(text):
    word_dict={}
    for char in text.lower():
        if char in word_dict:
            word_dict[char]+=1
        else:
            word_dict[char]=1
    return(word_dict)


#FUNCTION TO MAKE LIST OF DICTIONARY BASED ON HIGHEST CHAR COUNT
#making the key for the sort function (sorting based on what)
def sort_on(dict):
    return dict["count"]

#straight from text function
def alpha_list(text):
    list=[]
    for word in num_each_simple(text):
        if word.isalpha()==True:
            list.append({"char":word, "count":num_each_simple(text)[word]})
    list.sort(reverse=True, key=sort_on)
    return list

#from dictionary function
def alpha_list_dict(word_dict):
    list=[]
    for char,count in word_dict.items():
        if char.isalpha()==True:
            list.append({"char":char,"count":count})
    list.sort(reverse=True,key=sort_on)
    return list