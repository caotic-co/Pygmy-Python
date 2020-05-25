import unittest
from src.python.pygmypython.entry_point import main

class TestEntryPoint(unittest.TestCase):
    def test_main(self):
        return_code = main(["Hello", "World"])
        self.assertEqual(0, return_code)


if __name__ == '__main__':
    unittest.main()
