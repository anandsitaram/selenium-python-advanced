import unittest


# Set up Module - > A method called before the execution of any component of a module
def setUpModule():
    print("Set Up module")


# Set up Module - > A method called after the execution of all the components of a module
def tearDownModule():
    print("tear Down Module")


class TestScenario(unittest.TestCase):

    # Set up class - > Executes before all the tests in an individual class have run
    @classmethod
    def setUpClass(self):
        print("Setup Class ")

    # Tear Down class - > Executes after all the tests in an individual class has run
    @classmethod
    def tearDownClass(self):
        print("Tear down class ")

    # Set up - > Executes before every test method
    def setUp(self):
        print("SetupMethod")

    # Test One - > The name of every test method begins with "test"
    def test_one(self):
        print("test_one")

    # Tear Down - > Executes after every test method
    def tearDown(self):
        print("Tear Down method")

    # Test Two - > The name of every test method begins with "test"
    def test_two(self):
        print("test_one")

    # Test Three - > The name of every test method begins with "test"
    def test_three(self):
        print("test_three")
