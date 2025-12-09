def get_number_of_words_in_book(booktext):
    return len(booktext.split())


def count_characters(text):
    collection = {}
    text = text.lower()
    for ch in text:
        if ch in collection:
            collection[ch] += 1
        else:
            collection[ch] = 1
    return collection


def sort_dict(collection):
    out_list = list()
    for k in collection:
        out_list.append({"char": k, "num": collection[k]})
    out_list.sort(key=sort_on, reverse=True)
    return out_list


def sort_on(items):
    return items["num"]


def generate_report(text):
    word_count = get_number_of_words_in_book(text)
    collection = count_characters(text)
    sorted_list_of_dicts = sort_dict(collection)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_list_of_dicts:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")
