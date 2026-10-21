import random
import string

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+"

MIN_LENGTH = 4

COMMON_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "123456789",
    "12345", "1234", "111111", "1234567", "dragon",
    "123123", "baseball", "abc123", "football", "monkey",
    "letmein", "shadow", "master", "666666", "qwertyuiop",
    "123321", "mustang", "1234567890", "michael", "654321",
    "superman", "1qaz2wsx", "7777777", "121212", "000000",
    "admin", "root", "welcome", "login", "passw0rd",
}


def is_common(password: str) -> bool:
    return password.lower() in COMMON_PASSWORDS

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

    if is_common(password):
        return "weak"

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
