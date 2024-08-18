import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    
    def setUp(self):
        print("Setting up before a test")
    
    def tearDown(self):
        print("Cleaning up after a test")

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 1)

if __name__ == '__main__':
    unittest.main()
