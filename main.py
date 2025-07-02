from stats import count_words, count_characters, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 2:
        book_text = get_book_text(sys.argv[1])
        num_words = count_words(book_text)
        characters_dict = count_characters(book_text)
        sorted_list_dict = sort_dictionary(characters_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dict in sorted_list_dict:
            print(f"{dict['name']}: {dict['num']}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()