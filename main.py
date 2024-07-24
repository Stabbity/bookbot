def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = count_characters(text)
    sorted_counts = sort_character_count(letter_count)
    print_report(sorted_counts, num_words)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    letters = text.lower()
    letter_count = {}
    for x in letters:
        if x.isalpha():
            if x in letter_count:
                letter_count[x] = letter_count[x] + 1
            else:
                letter_count[x] = 1
    return letter_count

def sort_character_count(letter_count):
    letter_list = [{'char': char, 'num': count} for char, count in letter_count.items()]

    def sort_on(dict):
        return dict['num']

    letter_list.sort(reverse=True, key=sort_on)

    return letter_list

def print_report(letter_list, num_words):
    print(f"--- Begin report of books/frakenstein.txt ---")
    print(f"{num_words} words found in the document")
    for item in letter_list:
        print (f"the {item['char']} was found {item['num']} times")
    print("--- End Report ---)")


main()