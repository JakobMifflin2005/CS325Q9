def get_text(filepath): 
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def split_words(book):
    words = book.split()
    return len(words)

def split_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    letters = {}
    for x in book:
        char = x.lower()
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters

def found_common_words(book, common_words):
    book_words = book.lower().split()
    found_words = {}
    for word in common_words:
        count = book_words.count(word)
        if count > 0:
            found_words[word] = count
    return found_words


book_title = "words.txt"
book = get_text(book_title)
book_counts = count_letters(book)
word_count = split_words(book)
letter_count = count_letters(book)