def clean_word(word: str) -> str:
    return word.strip().lower()


def get_first_word(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    return clean_word(words[0])


sentence = "   PYTHON is amazing   "
print(get_first_word(sentence))