wordList = ["hello", "hey", "goodbye", "yo", "yes"]

def print_upper_words(words, word_starts_with):
    """Print words in a list that start with specific letters and make them uppercase."""
    for word in words:
         for letter in word_starts_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words(wordList, word_starts_with={'y', 'g'})