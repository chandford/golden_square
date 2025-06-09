from lib.gratitudes import Gratitudes

def test_gratitudes_returns_string():
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert type(result) == str

def test_add_single_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("community")
    result = gratitudes.format()
    assert result ==  "Be grateful for: community"

def test_add_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("community")
    gratitudes.add("wifi")
    gratitudes.add("sleep")
    result = gratitudes.format()
    assert result ==  "Be grateful for: community, wifi, sleep"

