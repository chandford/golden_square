from lib.greet import *

def test_greet():
    expected = "Hello, Char!"
    # Arrange, act, assert
    actual = greet("Char")
    assert actual == expected
