import unittest

class LoginTest(unittest.TestCase):
    def test_loginByEmail(self):
        print("Login by email")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("Login by Facebook")
        self.assertTrue(True)

    def test_loginByTwitter(self):
        print("Login by Twitter")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()