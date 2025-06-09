from lib.password_checker import PasswordChecker
import pytest

def test_long_password():
    checker = PasswordChecker()
    result = checker.check("12345678")
    assert result == True

def test_short_password_raises_exception():
    checker = PasswordChecker()
    with pytest.raises(Exception) as err:
        checker.check("123")
    error_message = str(err.value)
    assert error_message == "Invalid password, must be 8+ characters."