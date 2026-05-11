import pytest
import sys
@pytest.mark.sanity
def testlogin():
    print("Login successful")

@pytest.mark.xfail
def testloggoff():
    print("Logoff Successful")

@pytest.mark.skipif(sys.version_info < (3,15),reason="Requires python 3.10 and above")
def testcalculation():
    assert 2+2 == 3