import pytest

@pytest.fixture()
def setUp():
    print('Open URL to login')
    yield
    print('Closing browser after login')

def test_loginByEmail(setUp):
    print('This is login by email test')

def test_loginfacebook(setUp):
    print('This is login by Facebook test')

