import unittest


class AssertionsDemo(unittest.TestCase):

    def test_A(self):
        self.assertFalse(5 != 5)

    def test_B(self):
        self.assertTrue(5 != 5)

    def test_C(self):
        self.assertEqual("TestQA", "TestQA")

    def test_D(self):
        dict1 = {'Key1': 45, 'Key2': 35}
        dict2 = {'Key1': 45, 'Key2': 35}
        self.assertDictEqual(dict1, dict2)

    def test_F(self):
        self.assertNotEqual("Test", "test")

    def test_G(self):
        self.assertIs(int("45"), 45)

    def test_H(self):
        self.assertRaises(TypeError, 24, "BS")
