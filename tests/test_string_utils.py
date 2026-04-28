import pytest
from src.string_utils import StringUtils

class TestStringUtils:
    @pytest.fixture
    def string_utils(self):
        return StringUtils()

    def test_reverse_string(self, string_utils):
        assert string_utils.reverse("hello") == "olleh"
        assert string_utils.reverse("") == ""
        assert string_utils.reverse("a") == "a"

    def test_is_palindrome(self, string_utils):
        assert string_utils.is_palindrome("racecar") == True
        assert string_utils.is_palindrome("hello") == False
        assert string_utils.is_palindrome("A man a plan a canal Panama") == True
        assert string_utils.is_palindrome("") == True

    def test_count_words(self, string_utils):
        assert string_utils.count_words("hello world") == 2
        assert string_utils.count_words("") == 0
        assert string_utils.count_words("  hello world  ") == 2

    @pytest.mark.parametrize("text, char, expected", [
        ("hello", "l", 2),
        ("hello", "z", 0),
        ("", "a", 0),
        ("aaa", "a", 3)
    ])
    def test_count_character(self, string_utils, text, char, expected):
        assert string_utils.count_character(text, char) == expected

    def test_count_character_case_sensitive(self, string_utils):
        assert string_utils.count_character("Hello", "h") == 0
        assert string_utils.count_character("Hello", "H") == 1

    def test_reverse_with_special_characters(self, string_utils):
        assert string_utils.reverse("hello!@#") == "#@!olleh"

    def test_count_words_with_multiple_spaces(self, string_utils):
        assert string_utils.count_words("hello  world") == 2
        assert string_utils.count_words("   ") == 0