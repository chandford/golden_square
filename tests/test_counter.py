from lib.counter import Counter

def test_initial_counter_value():
    counter = Counter() # instantiate 
    actual = counter.report()
    assert actual == "Counted to 0 so far."

def test_counter_adds_single_int():
    counter = Counter()
    counter.add(28)
    actual = counter.report()
    assert actual == "Counted to 28 so far."


def test_counter_adds_positive_ints():
    counter = Counter()
    counter.add(2)
    counter.add(10)
    actual = counter.report()
    assert actual == "Counted to 12 so far."

def test_counter_adds_negative_ints():
    counter = Counter()
    counter.add(-1)
    counter.add(-10)
    counter.add(-20)
    actual = counter.report()
    assert actual == "Counted to -31 so far."

def test_counter_adds_mixed_ints():
    counter = Counter()
    counter.add(-1)
    counter.add(-2)
    counter.add(20)
    actual = counter.report()
    assert actual == "Counted to 17 so far."
