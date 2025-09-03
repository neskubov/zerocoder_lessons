import pytest
from main import count_vowels_in_string

@pytest.mark.parametrize("text, language, expected", [
    ("аоуиэяюуюиоеи", 'ru', 13),
    ("крпнгцшвтмсчтдлхзщф", 'ru', 0),
    ("крпнгцшвтмсчтдлхзщфЕУИяоеу", 'ru', 7),
    ("euioooaui", 'en', 9),
    ("sdgfhjklcvbnmxtr", 'en', 0),
    ("eruiosanjxebyIOsDGF", 'en', 8)
])


def test_count_vowels_in_string(text, language, expected):
    assert count_vowels_in_string(text, language) == expected

