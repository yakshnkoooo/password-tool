import random
import string

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+"

MIN_LENGTH = 4


def generate(
    length: int = 12,
    use_upper: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    if length < MIN_LENGTH:
        raise ValueError(f"Длина должна быть не меньше {MIN_LENGTH}")

    alphabet = LOWER
    if use_upper:
        alphabet += UPPER
    if use_digits:
        alphabet += DIGITS
    if use_symbols:
        alphabet += SYMBOLS

    return "".join(random.choice(alphabet) for _ in range(length))


def strength(password: str) -> str:
    if not password:
        return "empty"

    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in SYMBOLS for c in password):
        score += 1

    if score <= 2:
        return "weak"
    if score <= 4:
        return "medium"
    return "strong"
