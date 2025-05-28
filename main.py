def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def word_counter(string):
    count = string.split()
    return len(count)

def main():
    string = get_book_text("/home/grant/workspace/github.com/grantlukacs/bookbot/books/frankenstein.txt")
    count = word_counter(string)
    print(f"{count} words found in the document")

main()