def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not word:
        return False
    min_i = 0
    max_i = len(word) - 1

    while min_i < max_i:
        if word[min_i] != word[max_i]:
            return False
        min_i += 1
        max_i -= 1

    return True
