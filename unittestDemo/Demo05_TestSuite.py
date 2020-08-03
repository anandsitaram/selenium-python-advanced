import unittest

from unittestDemo.Demo02_Assertions import AssertionsDemo
from unittestDemo.Demo04_SkipTests import SkipTests

if __name__ == "__main__":
    unittest.main()
    # get all tests from AssertionsDemo class
    tc = unittest.TestLoader.loadTestsFromTestCase(AssertionsDemo)
    # get all tests from SkipTests class
    tc1 = unittest.TestLoader.loadTestsFromTestCase(SkipTests)

    # create a test suite combining tc and tc1
    test_suite = unittest.TestSuite([tc, tc1])
    # run the suite
    unittest.TextTestRunner(verbosity=1).run(test_suite)
