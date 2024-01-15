
def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path).lower()
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    write_report(text,num_words,sorted(list(chars_dict.items())))
    
def write_report(text, num_words, chars_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n\n")
    
    print(chars_list)
    for i in chars_list:
        print(f"The {i[0]} character was found {i[1]} times")
    
    print("--- End report ---")
    
    

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
        

def get_num_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

main()
