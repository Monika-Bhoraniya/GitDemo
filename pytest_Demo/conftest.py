import pytest

@pytest.fixture()
def setup():
    print("i will")
    yield
    print("i will execute first")
