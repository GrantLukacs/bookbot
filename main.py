from stats import word_counter
from stats import character_counter
from stats import sorter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = "/home/grant/workspace/github.com/grantlukacs/bookbot/books/frankenstein.txt"
    string = get_book_text(path)
    count = word_counter(string)
    print(f"{count} words found in the document")
    list = character_counter(string)
    sorted_list = sorter(list)
    #print(sorted_list)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for i in sorted_list:
        char = i["char"]
        num = i["num"]
        print(f"{char}: {num}")

    print("============= END ===============")

main()