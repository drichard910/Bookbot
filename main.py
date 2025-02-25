import sys
from stats import count_words_of_book, count_number_of_characters, sorted_list_of_characters

def get_book_text(path_to_file):
    #Use relative path to get the text of abook
    with open(path_to_file) as f:
        file_contents = f.read()
        # turn text into a string
    return file_contents

def main():
    book = sys.argv
    if len(book) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #grab the book file
    books_text = get_book_text(str(book[1]))
    print("============ BOOKBOT ============")
    print("Analyzing book found at ...")
    print("----------- Word Count ----------")
    print(f"Found {count_words_of_book(books_text)} total words")
    print("--------- Character Count -------")
    counted_nums = count_number_of_characters(books_text)
    ordered_characters = sorted_list_of_characters(counted_nums)
    for characters in ordered_characters:
        if characters[0].isalpha() == True:
            print(f"{characters[0]}: {characters[1]}")
    print("============= END ===============")
main()
    