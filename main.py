def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_content(path)

    print(f"---Begin report of {path}---")
    print(f"There are {count_words(file_contents)} words in this book")
    
    letters = count_letters(file_contents)
    for l in sorted(letters.items(), key=lambda x:x[1], reverse=True):
        print(f"The '{l[0]}' was found {l[1]} times")

def get_book_content(path):
    with open(path) as f:
        return f.read()

def count_words(content):
    return len(content.split())

def count_letters(content):
    lowered_content = content.lower()

    letters = {}
    for l in lowered_content:
        if l.isalpha():
            letters[l] = letters.get(l, 0) + 1

    return letters

#def sort_on(dict):
#    return dict["num"]

main()