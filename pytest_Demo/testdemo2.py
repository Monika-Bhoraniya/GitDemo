# Any pytest file should start with test_
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg = "hello"
    assert msg == "hi", "test failed, not match"



def test_SecondCreditCard():
   a = 4
   b = 6
   assert a+2 ==6, "Addtion"

@pytest.fixture()
def setup():
    print("i will be execute first")

def test_fixtureDemo():
    print("i will execute steps in fixtureDemo method")
