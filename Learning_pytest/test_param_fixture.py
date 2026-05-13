import pytest

# @pytest.fixture()
# def setup():
#     print("\nopen browser")
#     print("open the url for shopping website")
#     print("Buy items")
#     yield
#     print("\nexit cart")
#     print("exit the shopping website")
#     print("Close the browser")

@pytest.fixture(params=["a","b"])
def demo_fixture(request):
    return request.param
def testadditems(demo_fixture):
    print("Added items to cart")

def testremoveitems(demo_fixture):
    print("Removed items from cart")