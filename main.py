def main():
    book_path = "bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    sorted_num_letters = sort_dict(num_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for entry in sorted_num_letters:
        letter = entry["letter"]
        num = entry["num"]
        print(f"The {letter} character was found {num} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    lowered_text = text.lower()
    letters_num = {"a" : 0
        ,"b" : 0
        ,"c" : 0
        ,"d" : 0
        ,"e" : 0
        ,"f" : 0
        ,"g" : 0
        ,"h" : 0
        ,"i" : 0
        ,"j" : 0
        ,"k" : 0
        ,"l" : 0
        ,"m" : 0
        ,"n" : 0
        ,"o" : 0
        ,"p" : 0
        ,"q" : 0
        ,"r" : 0
        ,"s" : 0
        ,"t" : 0
        ,"u" : 0
        ,"v" : 0
        ,"w" : 0
        ,"x" : 0
        ,"y" : 0
        ,"z" : 0
        }
    for letter in [*lowered_text]:
        if letter in letters_num:
            letters_num[letter] += 1
        else :
            pass
    return letters_num

def sort_dict(dict):
    def sort_on(dict):
        return dict["num"]
    list = []
    for entry in dict :
        new_dict = {}
        new_dict["letter"] = entry
        new_dict["num"] = dict[entry]
        list.append(new_dict) 
    list.sort(key = sort_on, reverse=True)
    return list
main()
