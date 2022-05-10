import unittest
import numpy as np


def halfening(mylist):
    return [x/2 for x in mylist]


class TestSum(unittest.TestCase):

    def test_trials(self):
        a = 3.14
        b = np.pi
        c = np.array([2, 4, 8, 16, 32])
        self.assertNotEqual(a, b, 'Values not equal')
        self.assertIsInstance(a, float, 'Not a float')
        self.assertLessEqual(b, 4, 'Greater than 4')
        self.assertIsNotNone(c, 'Error: object is None')
        self.assertIsInstance(c, np.ndarray)
    

    def test_halfening_fn(self):
        z = [100, 50, 25, 12.5]
        self.assertEqual(len(z), len(halfening(z)), 'Not same length')
        self.assertRaises(TypeError, halfening, str, 'Did not raise the expected TypeError')
        self.assertRegex('My name is Baby Yoda'.lower(), 'yoda', 'Error: substring not contained in mother string')


if __name__=='__main__':
    unittest.main()