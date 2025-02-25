def count_words_of_book(text):
    #Find out how many words are in a book
    num_of_words = 0
    words_list = text.split()
    #turns the str into a list
    for num in words_list:
        num_of_words += 1
    return num_of_words

def count_number_of_characters(text):
    #Find out how many of each character is in a book
    counted_characters = {}
    lowered_text = text.lower()

    for i in lowered_text:
        if i not in counted_characters:
            counted_characters[i] = 1
        else:
            counted_characters[i] += 1
    return counted_characters

def sort_by_count(tuple_items):
    return tuple_items[1]

def sorted_list_of_characters(text):
    #Sort the dictionary of the book
    text_listed = list(text.items())
    text_listed.sort(key=sort_by_count, reverse=True)
    return text_listed