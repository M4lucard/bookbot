from stats import count_characters, get_number_of_words_in_book, sort_dict, generate_report
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    text = get_book_text(sys.argv[1])
    # text = get_book_text("books/frankenstein.txt")
    # word_count = get_number_of_words_in_book(text)
    # collection = count_characters(text)

    # print(f"Found {word_count} total words")
    # print(f"{collection}")
    
    generate_report(text)
    
main()