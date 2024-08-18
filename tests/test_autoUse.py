import pytest

@pytest.fixture(autouse=True)
def always_setup():
    print("Setting up for every test")

def test_example_1():
    assert True

def test_example_2():
    assert True

