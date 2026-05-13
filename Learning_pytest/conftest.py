import pytest


@pytest.fixture()
def setup():
    print("\nopen browser")
    print("open the url for shopping website")
    print("Buy items")
    yield
    print("\nexit cart")
    print("exit the shopping website")
    print("Close the browser")
