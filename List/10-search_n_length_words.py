# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

def search_words_len(words, length):
    n_words = list()
    for i in words:
        list_i = list(i)
        if len(list_i) > length:
            n_words.append(i)
    return n_words


words = "Write a Python program to find the list of words that are longer than n from a given list of words."
word_list = words.split(" ")
print(word_list)
print(search_words_len(word_list, length=3))
