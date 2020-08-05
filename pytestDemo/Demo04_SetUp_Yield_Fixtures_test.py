import pytest


# Runs before (statements before yield) and after (statements after yield) every test method
@pytest.yield_fixture()
def setUp_yield():
    print("\n")
    print("Set up !!!")
    yield
    print("Tear down !!!")


def test_methodG(setUp_yield):
    print("test method G")


def test_methodH(setUp_yield):
    print("test method H")
