def main():
    book_location = 'books/frankenstein.txt'
    book_text = None

    book_text = get_book_text(book_location)
    number_of_words = count_words(book_text)
    print(f"{number_of_words} in the document")


def get_book_text(path):
    with open(path) as book:
        text = book.read()
        return text

def count_words(book_text):
    total_words = book_text.split()
    return len(total_words)


main()