import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nopen browser")
    print("open the url for shopping website")
    print("Buy items")
    yield
    print("\nexit cart")
    print("exit the shopping website")
    print("Close the browser")

def testadditems():
    print("Added items to cart")

def testremoveitems():
    print("Removed items from cart")

