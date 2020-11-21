import random
import string


def get_random_string_of_length(length: int, lowercase=True, uppercase=True, numbers=True):
    letters = ''
    if not (lowercase or uppercase or numbers):
        raise Exception("Empty character set given")

    letters = letters + string.ascii_lowercase if lowercase else letters
    letters = letters + string.ascii_uppercase if uppercase else letters
    letters = letters + string.digits if numbers else letters

    return ''.join(random.choice(letters) for _ in range(length))
