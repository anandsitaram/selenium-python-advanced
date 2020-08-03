import unittest


class SkipTests(unittest.TestCase):
    count = 9

    @unittest.skip
    def test_A(self):
        self.assertFalse(5 != 5)

    @unittest.skip("Not requirement")
    def test_B(self):
        self.assertTrue(5 == 5)

    @unittest.skipIf(count % 2 == 0, "Not a even number")
    def test_C(self):
        self.assertEqual("TestQA", "TestQA")

    @unittest.skipIf(count % 3 == 0, "Not a divisible by 3")
    def test_D(self):
        self.assertEqual("TestQA", "TestQA")

    @unittest.skipUnless(count*3 == 11, "Not Equal")
    def test_E(self):
        self.assertEqual("TestQA", text="TestQA")