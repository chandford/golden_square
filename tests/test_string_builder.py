from lib.string_builder import StringBuilder

def test_initial_value():
    builder = StringBuilder()
    assert builder.size() == 0
    assert builder.output() == ""

def test_add_single_char_string():
    builder = StringBuilder()
    builder.add("C")
    assert builder.size() == 1
    assert builder.output() == "C"

def test_add_multi_char_string():
    builder = StringBuilder()
    builder.add("chocolate")
    assert builder.size() == 9
    assert builder.output() == "chocolate"

def test_add_multiple_strings():
    builder = StringBuilder()
    builder.add("chocolate")
    assert builder.size() == 9
    assert builder.output() == "chocolate"
    builder.add("milk")
    builder.add("shake")
    assert builder.size() == 18
    assert builder.output() == "chocolatemilkshake"
