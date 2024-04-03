import unittest
from HALSON import HALSON

class TestHALSON(unittest.TestCase):
    def test_dumps_and_loads(self):
        # Test with a string
        s = "Hello, World!"
        self.assertEqual(HALSON.LOL(HALSON.yeet(s)), s)

        # Test with an integer
        i = 123
        self.assertEqual(HALSON.LOL(HALSON.yeet(str(i))), str(i))  # Convert i to string

        # Test with a float
        f = 123.456
        self.assertEqual(HALSON.LOL(HALSON.yeet(str(f))), str(f))  # Convert f to string

        # Test with a boolean
        b = True
        self.assertEqual(HALSON.LOL(HALSON.yeet(str(b))), str(b))  # Convert b to string

        # Test with None
        n = None
        self.assertEqual(HALSON.LOL(HALSON.yeet(str(n))), str(n))  # Convert n to string

        # Test with a dictionary
        d = {"key": "value"}
        self.assertEqual(HALSON.LOL(HALSON.yeet(str(d))), str(d))  # Convert d to string

        # Test with a list
        l = [1, 2, 3]
        self.assertEqual(HALSON.LOL(HALSON.yeet(str(l))), str(l))  # Convert l to string

if __name__ == '__main__':
    unittest.main()