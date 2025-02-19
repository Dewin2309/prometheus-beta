import pytest
from src.text_splitter import split_text_to_words

def test_basic_word_splitting():
    assert split_text_to_words("HelloWorld") == ["Hello", "World"]
    assert split_text_to_words("helloWorld") == ["hello", "World"]

def test_punctuation_handling():
    assert split_text_to_words("Hello,World!") == ["Hello", ",", "World", "!"]
    assert split_text_to_words("hello,world") == ["hello", ",", "world"]

def test_capital_letter_sequences():
    assert split_text_to_words("HelloUNITED") == ["Hello", "UNITED"]
    assert split_text_to_words("ABCWord") == ["ABC", "Word"]

def test_mixed_scenarios():
    assert split_text_to_words("Hello,WorldABC") == ["Hello", ",", "World", "ABC"]
    assert split_text_to_words("hi!ThereHowAreYou?") == ["hi", "!", "There", "How", "Are", "You", "?"]

def test_empty_input():
    assert split_text_to_words("") == []

def test_single_word():
    assert split_text_to_words("hello") == ["hello"]
    assert split_text_to_words("Hello") == ["Hello"]

def test_complex_scenarios():
    assert split_text_to_words("JavaProgrammingLanguage") == ["Java", "Programming", "Language"]
    assert split_text_to_words("OpenAIGPT4Model") == ["Open", "AI", "GPT", "4", "Model"]