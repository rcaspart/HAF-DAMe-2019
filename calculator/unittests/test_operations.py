import sys

print
sys.executable
print
"\n".join(sys.path)

import unittest
from calculator import operations
from calculator import parse_input


class TestOperations(unittest.TestCase):
    """Standard tests for the operations"""
    def test_add_int(self):
        """Test if the add operation returns the correct result for a test case"""
        self.assertEqual(operations.add(3,4), 7)

    def test_subtract_int(self):
        """Test if the subtract operation returns the correct result for a test case"""
        self.assertEqual(operations.subtract(7,4), 3)

    def test_multiply_int(self):
        """Test if the mulitply operation returns the correct result for a test case"""
        self.assertEqual(operations.multiply(3,4), 12)

    def test_devide_int(self):
        """Test if the devide operation returns the correct result for a test case"""
        self.assertEqual(operations.devide(8,4), 2)

class TestParser(unittest.TestCase):
    """Tests for the parser"""
    def test_parse_add(self):
        self.assertEqual(parse_input.parse(["1", "+", "2"]), 3)

#    def test_exception(self):
#        with self.assertRaises(Exception):
#            parse_input.parse(["-", "2"])

    def test_parse_subtract(self):
        self.assertEqual(parse_input.parse(["3", "-", "2"]), 1)

    def test_parse_add2(self):
        self.assertEqual(parse_input.parse(["1", "+", "2", "+", "3"]), 6)

#    def test_parse_add3(self):
#        self.assertEqual(parse_input.parse(["1", "+", "2", "*", "3"]), 7)


if __name__ == '__main__':
    unittest.main()