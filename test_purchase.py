import pytest

@pytest.fixture()
def setUp():
    print("setup started")
    yield
    print("exited")

def test_AddItemToCart(setUp):
    print("added successfully")

def test_RemoveItemToCart(setUp):
    print("removed successfully")