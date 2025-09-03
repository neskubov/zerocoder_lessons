def count_vowels_in_string(text, language='ru'):
    match language:
        case 'ru':
            vowels = "аеёиоуыэюя"
        case 'en':
            vowels = "aeiou"

    result = sum([text.lower().count(vowel) for vowel in vowels])
    return result

