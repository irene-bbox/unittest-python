# Python Unit Tests

## Getting started
#### Structure
We will use the Python built-in module `unittest` to practice writing simple unit tests in Python.

:warning: The correct structure of an assert statement is `assertSomething(a, b, msg='custom message')`, where
* `a` the value you're testing
* `b` the expected value
* `msg` a custom error message to be returned if the test fails
  
> All the assert methods accept a *msg* argument that, if specified, is used as the error message on failure

#### Example
```bash
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(4, 7, 6), 17, msg='ERROR: incorrect sum')

if __name__ == '__main__':
    unittest.main()
```

#### Test Runner :electric_plug: :snail: :computer:
There are many ways to execute unit tests. Assume you named your test file *test.py*. In command line, run:
 - `python test.py` executes the test runner by discovering all classes in this file that inherit from *unittest.TestCase*. If you have a single test file named *test.py*, calling `python test.py` is a great way to get started. Add the flag `-v` to get a more descriptive output.
 - `python -m unittest test` executes the same test module (called *test*) via the command line
 - `python -m unittest -v test` you can add flag, like `-v` for *verbose* to return more descriptive outputs
 - `python -m unittest discover` also executes via the *unittest* command line with one difference: instead of providing the name of a module containing tests, request an auto-discovery

## Assert Methods
#### Most Commonly Used 

| Method | Checks that | Checks for |
|:-|:-|:-:|
| assertEqual(a, b) | `a == b` | **equality** |
| assertNotEqual(a, b) | `a != b` | |
| assertTrue(x) | `bool(x)` is `True` | **truth** |
| assertFalse(x) | `bool(x)` is `False` | |
| assertIs(a, b) | `a is b` | **identity** |
| assertIsNot(a, b) | `a is not b` | |
| assertIsNone(x) | `x is None` | **None Type** |
| assertIsNotNone(x) | `x is not None` | |
| assertIn(a, b) | `a in b` | **belonging** |
| assertNotIn(a, b) | `a not in b` | |
| assertIsInstance(a, b) | `isinstance(a, b)` | **Type check** |
| assertNotIsInstance(a, b) | `not isinstance(a, b)` | |

#### Specific Checks 

| Method | Checks that | Checks for |
|:-|:-|:-:|
| assertAlmostEqual(a, b, places=7, <br/> msg=None, delta=None) | `a ~ b` | **equality** |
| assertGreater(a, b) | `a > b` | **value size** |
| assertGreaterEqual(a, b) | `a >= b` | |
| assertLess(a, b) | `a < b` | |
| assertLessEqual(a, b) | `a <= b` | |
| assertRegex(test, regex, msg=None) | `r.search(s)` | **coincidence** |
| assertCountEqual(a, b) | a and b have the same <br/> elements in the same number, <br/> regardless of their order. | **similarity** |

#### Exceptions, Warnings, Log messages 

| Method | Checks that | Checks for |
|:-|:-|:-:|
| assertRaises(exception, callable, <br/> *args, **kwds, msg=None) | `fun(*args, **kwds)` raises exc | **exceptions** |


## Outputs

A Python unit test always returns one of 3 possible outcomes:
* `success` --> the tested code passed all tests
* `failure` --> some of the tested code failed to pass the test
* `error` --> the testing code broke somewhere, an exception was raised, and the tests could not be executed properly. 
