import pytest

#Run One time before module
@pytest.yield_fixture(scope="module")
def oneTime_setUp_yield():
    print("\n")
    print("oneTime_setUp!!!")
    yield
    print("oneTimeTear down !!!")


@pytest.yield_fixture()
def setUp_yield():
    print("\n")
    print("Set up !!!")
    yield
    print("Tear down !!!")


def test_methodM(oneTime_setUp_yield, setUp_yield):
    print("test method M")


def test_methodN(oneTime_setUp_yield, setUp_yield):
    print("test method N")
