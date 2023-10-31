def capitalize(word: str) -> str:
    first_letter = word[0].upper()
    remainder = word[1:]
    return first_letter + remainder
