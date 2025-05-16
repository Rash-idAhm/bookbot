def count_words(text):
    # Use split() to get a list of words
    words = text.split()
    # Count the number of words
    num_words = len(words)
    # Return the count
    return num_words

def char_count(book_text):
    characters_and_count = {}

    for char in book_text:
        char = char.lower()
        
        if char in characters_and_count:
            characters_and_count[char] += 1
        else:
            characters_and_count[char] = 1
    return characters_and_count

def sort_on_num(char_num_list):
    return char_num_list["num"]

def sort_list(book_text):
    char_num_list = []

    for char, num in book_text.items():
        if char.isalpha():
            char_num_list.append({"char": char,"num": num})
        
    char_num_list.sort(reverse=True, key=sort_on_num)
    return char_num_list

