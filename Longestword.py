def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

# Example usage
print(longest_word("Python is an amazing programming language"))