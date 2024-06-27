"""Tests for the colortext module."""

from io import StringIO

from colortext import print_color_text, color_text


def test_print_color_text():
    """Test the print_color_text function."""
    with StringIO() as out:
        text = "Hello, World!"
        print_color_text(text, color="red", style="bold", file=out)
        assert out.getvalue() == "\x1b[01;31mHello, World!\x1b[0m\n"


def test_color_text():
    """Test the color_text decorator."""

    @color_text(color="green", style="underline")
    def get_text():
        return "Hello, World!"

    assert get_text() == "\x1b[04;32mHello, World!\x1b[0m"
