# -- Setup and Teardown: executed before and after execute each method
# -- setUpClass and tearDownClass: executed before and after execute each class
# -- setUpModule and tearDownModule: executed before and after execute each module

import unittest

class AppTesting(unittest.TestCase):

    # create a Setup method which is executed before running other tests
    @classmethod
    def setUp(self):
        print("========= this is the setup test ===============")

    # create a teardown method which is executed after running other tests
    @classmethod
    def tearDown(self):
        print("========= this is teardown method =============")

    def test_search1(self):
        print("testing 1")
    
    def test_search2(self):
        print("testing 2")

    def test_search3(self):
        print("testing 3")

    def test_search4(self):
        print("testing 4")

if __name__ == "__main__":
    unittest.main()