

from collections import Counter
import nltk

nltk.download('punkt', quiet=True)

def word_count(text):
    """Returns the number of words in the text."""
    words = nltk.word_tokenize(text)
    return len(words)

def char_count(text):
    """Returns the number of characters in the text."""
    return len(text)

def most_common_words(text, n=3):
    """Returns the n most common words in the text."""
    words = nltk.word_tokenize(text.lower())
    return Counter(words).most_common(n)

def to_uppercase(text):
    """Converts text to uppercase."""
    return text.upper()

def to_lowercase(text):
    """Converts text to lowercase."""
    return text.lower()
