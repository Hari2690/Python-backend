import unittest
from src.your_package import module

class TestModule(unittest.TestCase):
    def test_example_function(self):
        self.assertEqual(module.example_function(), "Hello from module!")

if __name__ == "__main__":
    unittest.main()
