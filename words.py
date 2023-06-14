def print_upper_words(word_list, letter):
    """prints every word capitalized"""
    for word in word_list:
        if word[0].upper() == letter.upper():
            print(word)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], "h")
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], "Y")