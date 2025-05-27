import collections
import pprint

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_path):
    words = get_book_text(file_path)
    word_list = words.split()
    num_words = len(word_list)
    return num_words

def split_dictionary(original_dict):
    list_of_dictionaries = []
    for key, value in original_dict.items():
        list_of_dictionaries.append({'char': key, 'num': value})
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries

def sort_on(dict):
    return dict["num"]

def get_num_chars(file_path):
    with open(file_path) as info:
        count = collections.Counter(info.read().lower())
#        print(type(count))
        num_char_dict = dict(count)
#        value = pprint.pformat(count)
        value = split_dictionary(num_char_dict)
        return value
    