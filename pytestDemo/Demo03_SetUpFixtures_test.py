import pytest

# Runs before every test method
@pytest.fixture()
def setUp():
    print("\n")
    print("Set up method!!!")


def test_methodA(setUp):
    print("test method A")


def test_methodB(setUp):
    print("test method B")
