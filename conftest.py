import pytest

@pytest.fixture(scope="session", autouse=True)
def setUp():
    print("Open Amazon app")
    print("user logged in")
    yield
    print("user logged out")
    print("Close amazon app")