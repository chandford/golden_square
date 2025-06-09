from lib.present import Present
import pytest

def test_wrap():
    present = Present()
    present.wrap("gift")
    assert present.contents == "gift"

def test_wrap_raises_exception():
    present = Present()
    present.wrap("gift")
    with pytest.raises(Exception) as err:
        present.wrap("bonus gift")
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

def test_wrap_prserves_value():
    present = Present()
    present.wrap("gift")
    present.unwrap()
    with pytest.raises(Exception) as err:
        present.wrap("air")
    assert present.contents == "gift"

def test_unwrap():
    present = Present()
    present.wrap("gift")
    result = present.unwrap()
    assert result == "gift"

def test_unwrap_raises_exception():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."

