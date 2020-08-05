import pytest


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


@pytest.mark.run(order=3)
def test_method1(oneTime_setUp_yield, setUp_yield):
    print("test method 1")


@pytest.mark.run(order=4)
def test_method2(oneTime_setUp_yield, setUp_yield):
    print("test method 2")


@pytest.mark.run(order=5)
def test_method3(oneTime_setUp_yield, setUp_yield):
    print("test method 3")


@pytest.mark.run(order=1)
def test_method4(oneTime_setUp_yield, setUp_yield):
    print("test method 4")


@pytest.mark.run(order=0)
def test_method5(oneTime_setUp_yield, setUp_yield):
    print("test method 5")
