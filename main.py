def main():
    book_location = 'books/frankenstein.txt'
    book_text = None

    book_text = get_book_text(book_location)
    number_of_words = count_words(book_text)
    number_of_characters = count_characters(book_text)
    converted_list = convert_dic(number_of_characters)
    converted_list.sort(reverse=True, key=sort_on)

    print_report(book_location, number_of_words, converted_list)
    ##print(converted_list)
    ##print(number_of_characters)
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

def convert_dic(dic):
    tempList = []
    for character in dic:
        tempDic = {
            character:dic[character]
        }
        tempList.append(tempDic)
    return tempList

def sort_on(dict):
    for character in dict:
        return dict[character]

def print_report(location, number_of_words, converted_list):
    print(f"--- Begin report of {location} ---")
    print(f"{number_of_words} words found in the document")

    for i in range(0, len(converted_list)):
        items = converted_list[i].items()
        for k, v in items:
            if(k.isalpha()):
                print(f"The {k} character was found {v} times")
    print("--- End report ---")

main()