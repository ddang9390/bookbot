def main():
    file_contents = get_book_content("books/frankenstein.txt")
    print(f"There are {count_words(file_contents)} words in this book")
    print(count_letters(file_contents))

def get_book_content(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(content):
    return len(content.split())

def count_letters(content):
    lowered_content = content.lower()

    letters = {}
    for l in lowered_content:
        letters[l] = letters.get(l, 0) + 1

    return letters

main()