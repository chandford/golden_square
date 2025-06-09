from lib.report_length import *

def test_report_length_returns_string():
    expected = "This string was 6 characters long."
    actual = report_length("Maggie")
    assert type(actual) == str


def test_report_length_output():
    expected_1 = "This string was 6 characters long."
    actual_1 = report_length("Maggie")
    expected_2 = "This string was 7 characters long."
    actual_2 = report_length("Pytest!")
    assert actual_1 == expected_1
    assert actual_2 == expected_2