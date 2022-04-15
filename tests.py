from functions import volume_cylinder
import unittest


# This is a 'test case' subclassing multiple individual tests
class TestFunc(unittest.TestCase):

    # Each ndividual unit of testing is defined as a method (a function taking 'self' as parameter) whose name starts with 'test_'
    # This naming convention informs the test runner about which methods represent tests
    def test_volume_cylinder(self):
        
        # Specifically, we want to check for the following:
        # ensure the output is a float OR int
        self.assertIsInstance(volume_cylinder(2, 4), (float, int), 'ERROR: output volume is not a float')

        # ensure the output is not a None type
        self.assertIsNotNone(volume_cylinder(2, 4), 'ERROR: volume is a None type')

        # ensure the ourput is always positive, b/c volume is positive
        self.assertTrue(volume_cylinder(3, -6) > 0)

        # ensure the output volume is positive even when negative radii and heights are passed
        self.assertGreater(volume_cylinder(-2, 7), 0, 'ERROR: non-positive volume')
        self.assertGreaterEqual(volume_cylinder(-2, 0), 0, 'ERROR: non-positive volume')

        # ensure the output is zero if either the radius or the height is zero
        self.assertEqual(volume_cylinder(0, 5), 0, 'ERROR: volume != zero although height is zero')
        self.assertEqual(volume_cylinder(8, 0), 0, 'ERROR: volume != zero although radius is zero')
        
        # # check for identity: it should output a 0.0 float - I DON'T UNDERSTAND THIS ASSERT METHOD JUST YET!
        # self.assertIs(volume_cylinder(8, 0), 0.0, 'ERROR: not same object')

        # ensure the volume is as expected for some test values of radius and height
        self.assertEqual(volume_cylinder(2, 2), 25.12, 'ERROR: volume mismatch')
        self.assertAlmostEqual(round(volume_cylinder(3, 5), 2), 141.3) # call round() to make it equal
        self.assertAlmostEqual(volume_cylinder(3, 5), 141.3, places=1) # specify decimal places
        self.assertNotAlmostEqual(volume_cylinder(3, 5), 141.33, places=2) 
        self.assertAlmostEqual(volume_cylinder(3, 5), 141.25, delta=0.6) # define max allowed delta

        # ensure the input param are of type int OR float and nothing else. 
        self.assertIsInstance(volume_cylinder(3, 5), float, 'ERROR: output volume is not a float')
        # ensure it raises an error when passing a string
        with self.assertRaises(TypeError):
            volume_cylinder(2, str)

        # The assertRaises method:
        # - passes the test if the expected exception is raised
        # - it returns an error if another exception is raised
        # - fails the test if no exception is raised

        # with self.assertRaises(ValueError):
        #     volume_cylinder(2, str) 
        # |--> this returns an ERROR, beause it's raising a TypeError, instead of the expected ValueError

        # ensure the functions handles 'string' input parameters by raising an exception
        # the test is passed if the function 'volume_cylinder' raises exceptions
        self.assertRaises(TypeError, volume_cylinder, str) 

        # ensure 2 sequences contain the same elements regardless of their order
        self.assertCountEqual([1,2,True,'hello'], ['hello',2,1,True], 'ERROR: lists are different')

        # test out assertRegex
        self.assertRegex('abc', 'a') # pass
        self.assertRegex('abc', 'B') # fail
        self.assertRegex('abc', 'c') # pass
        self.assertRegex('abc', 'd') # fail

if __name__ == '__main__':
    unittest.main()