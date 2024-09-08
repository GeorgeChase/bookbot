def main():
    book_location = 'books/frankenstein.txt'
    book_text = None

    book_text = get_book_text(book_location)
    number_of_words = count_words(book_text)
    number_of_characters = count_characters(book_text)
    print(number_of_characters)
    ##print(f"{number_of_words} in the document")


def get_book_text(path):
    with open(path) as book:
        text = book.read()
        return text

def count_words(book_text):
    total_words = book_text.split()
    return len(total_words)

def count_characters(book_text):
    char_count = {}
    all_words = book_text.split()
    for word in all_words:
        word = word.lower()
        for character in word:
            if(character not in char_count):
                char_count[character] = 1
            else:
                char_count[character] += 1
    return char_count


main()