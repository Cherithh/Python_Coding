import pytest

@pytest.mark.parametrize("a,b,final",[(2,7,9),(4,4,8),(1,4,5)])
def test_addmark(a,b,final):
    assert a+b == final