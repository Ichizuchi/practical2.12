import re


def hyphen_consecutive_decorator(func):
    def wrapper(*args, **kwargs):
        result1 = func(*args, **kwargs)
        result1 = re.sub(r'-+', '-', result1)
        return result1

    return wrapper


@hyphen_consecutive_decorator
def to_lat(cyrillic_string):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
         'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
         'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
         'ю': 'yu',
         'я': 'ya'}

    cyrillic_string = cyrillic_string.lower()
    result1 = ''
    for char in cyrillic_string:
        if char.isalpha():
            result1 += t.get(char, char)
        elif char in "!?:;.,_":
            result1 += '-'
        else:
            result1 += char

    return result1


# Example usage
cyrillic_input = "Гайчук Дарья Дмитриевна."
result = to_lat(cyrillic_input)
print(result)
