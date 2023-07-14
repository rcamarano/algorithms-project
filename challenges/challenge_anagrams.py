def split_compare(str):
    if len(str) <= 1:
        return str

    str_mid = len(str) // 2
    str_left = split_compare(str[:str_mid])
    str_right = split_compare(str[str_mid:])
    return compare(str_left, str_right)


def compare(str_left, str_right):
    result = []
    i = j = 0

    while i < len(str_left) and j < len(str_right):
        if str_left[i] < str_right[j]:
            result.append(str_left[i])
            i += 1
        else:
            result.append(str_right[j])
            j += 1

    while i < len(str_left):
        result.append(str_left[i])
        i += 1

    while j < len(str_right):
        result.append(str_right[j])
        j += 1

    return result


def compare_str(string):
    # Converte a string para letras minúsculas, remove espaços em branco
    # e converte em lista
    list_chars = list(string.lower().replace(' ', ''))
    sort_chars = split_compare(list_chars)
    return ''.join(sort_chars)


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return '', '', False

    first_sort = compare_str(first_string)
    sec_sort = compare_str(second_string)

    if first_sort == sec_sort:
        return first_sort, sec_sort, True
    else:
        return first_sort, sec_sort, False
