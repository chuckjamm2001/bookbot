from stats import get_num_words
from stats import get_num_chars
import sys


#file_path = "books/frankenstein.txt"
#file_path = sys.argv[1]

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_path)} total words")
    print("--------- Character Count -------")
    list_of_dicts = get_num_chars(file_path)
#    print(type(list_of_dicts[0]))
    for dict in list_of_dicts:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")
#    print(get_num_chars(file_path))
    print("============= END ===============")

main()
