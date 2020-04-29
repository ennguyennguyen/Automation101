# -- Skipping test
import unittest

class SkipTest(unittest.TestCase):

    # -- using a decorator to skip test
    @unittest.SkipTest
    def test_func1(self):
        print("Test function 1")

    # -- using a skip reason
    @unittest.skip("I'm skipping test because this case is not ready")
    def test_func2(self):
        print("Test function 2")

    # -- using a condition
    @unittest.skipIf(1 == 1, "skip because of the condition")
    def test_func3(self):
        print("Test function 3")

    def test_func4(self):
        print("Test function 4")

    def test_func5(self):
        print("Test function 5")

if __name__ == "__main__":
    unittest.main()

