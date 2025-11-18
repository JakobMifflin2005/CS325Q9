import pytest
from textanalyzer import get_text
from textanalyzer import split_words    
from textanalyzer import count_letters
from textanalyzer import found_common_words
def test_get_text():
    text = get_text("words.txt")
    assert "Hello World" in text
def test_split_words():
    text = "Hello World Hello"
    assert split_words(text) == 3   
def test_count_letters():
    text = "aabbc"
    letter_counts = count_letters(text)
    assert letter_counts['a'] == 2
    assert letter_counts['b'] == 2
    assert letter_counts['c'] == 1
def test_found_common_words():
    text = "hello world hello"
    common_words = ["hello", "world", "test"]
    found_words = found_common_words(text, common_words)
    assert found_words["hello"] == 2
    assert found_words["world"] == 1
    assert "test" not in found_words