def main():
    with open("bookbot/books/frankenstein.txt") as frankenstein:
        file_contents = frankenstein.read()
        print(file_contents)

main()