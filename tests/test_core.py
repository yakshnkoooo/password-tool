import random

import pytest

from password_tool.core import (
    generate,
    strength,
    is_common,
    MIN_LENGTH,
    DIGITS,
    SYMBOLS,
)


# ---------- generate ----------

def test_generate_default_length():
    random.seed(42)
    assert len(generate()) == 12


def test_generate_custom_length():
    random.seed(42)
    assert len(generate(20)) == 20


def test_generate_too_short():
    with pytest.raises(ValueError):
        generate(MIN_LENGTH - 1)


def test_generate_only_letters():
    random.seed(42)
    pwd = generate(20, use_digits=False, use_symbols=False)
    assert pwd.isalpha()


def test_generate_only_digits_and_lower():
    random.seed(42)
    pwd = generate(20, use_upper=False, use_symbols=False)
    assert all(c in DIGITS or c.islower() for c in pwd)


def test_generate_with_symbols_allowed_chars():
    random.seed(42)
    pwd = generate(50, use_symbols=True)
    assert all(c.isalnum() or c in SYMBOLS for c in pwd)


# ---------- strength ----------

def test_strength_empty():
    assert strength("") == "empty"


def test_strength_weak_short():
    assert strength("abc") == "weak"


def test_strength_weak_only_lowercase_long():
    assert strength("abcdefghijklmnopqrst") == "weak"


def test_strength_medium():
    # len>=8 (+1), mixed case (+1), digit (+1) = 3 -> medium
    assert strength("Abcdefg1") == "medium"


def test_strength_strong():
    assert strength("Abcdefgh1234!@#") == "strong"

# ---------- is_common ----------

def test_is_common_known_passwords():
    assert is_common("123456") is True
    assert is_common("password") is True
    assert is_common("qwerty") is True


def test_is_common_case_insensitive():
    assert is_common("PASSWORD") is True
    assert is_common("Qwerty") is True


def test_is_common_unknown_password():
    assert is_common("xK9!mP2#qL7@nR4$") is False
    assert is_common("MyUniquePass123") is False


def test_strength_rejects_common_passwords():
    assert strength("123456789") == "weak"
    assert strength("password") == "weak"
    assert strength("qwerty") == "weak"
