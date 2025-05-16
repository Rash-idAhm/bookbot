import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import count_words
from stats import char_count
from stats import sort_list

def get_book_text(filepath):
    with open(filepath) as w:
        words = w.read()
    return words
    
def main():
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    char_counts = char_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = char_count(text)
    sorted_char_list = sort_list(char_counts)
    for c in sorted_char_list:
        print(f"{c['char']}: {c['num']}")
    print("============= END ===============")
main()




        

