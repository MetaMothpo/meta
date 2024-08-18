import pytest

@pytest.fixture
def setup_and_teardown():
    # Setup: Open a file
    file = open("testfile.txt", "w")
    yield file  # Give the file to the test
    # Teardown: Close the file after the test
    file.close()

def test_file_write(setup_and_teardown):
    file = setup_and_teardown
    file.write("Hello, world!")
    file.seek(0)
    assert file.read() == "Hello, world!"
