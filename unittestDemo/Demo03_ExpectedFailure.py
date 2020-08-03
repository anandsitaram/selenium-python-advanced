import unittest


class ExpectedFailure(unittest.TestCase):

    @unittest.expectedFailure
    def test_H(self):
        self.assertRaises(TypeError, 24, "BS")
