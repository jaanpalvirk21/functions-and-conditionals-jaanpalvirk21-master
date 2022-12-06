"""Test module for the functions and conditionals assignment."""

from main import *


def test_format_name():
    """Test the format_name function."""
    result = format_name("Ernest", "Hemingway")
    expected = "Name: Hemingway, Ernest"
    assert(expected == result)
    
    result = format_name("", "Madonna")
    expected = "Name: Madonna"
    assert(expected == result)
    
    result = format_name("Voltaire", "")
    expected = "Name: Voltaire"
    assert(expected == result)
    
    result = format_name("", "")
    expected = ""
    assert(expected == result)


def test_get_seconds():
    """Test the get_seconds function."""
    assert(3723 == get_seconds(1,2,3))


def test_color_translator():
    """Test the color_translator function."""
    assert("#0000ff" == color_translator("blue"))
    assert("unknown" == color_translator("yellow"))
    assert("#ff0000" == color_translator("red"))
    assert("unknown" == color_translator("black"))
    assert("#00ff00" == color_translator("green"))
    assert("unknown" == color_translator(""))


def test_convert_degrees():
    """Test the convert_degrees function."""
    assert(62.6 == convert_degrees(17))
    assert(96.8 == convert_degrees(36))


def test_average_size():
    """Test the average_size function."""
    assert("The average size is: 20839.2" == average_size())
