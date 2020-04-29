import unittest

class PaymentTest(unittest.TestCase):
    def test_payByCash(self):
        print("Pay by cash")
        self.assertTrue(True)

    def test_payByCredit(self):
        print("Pay by credit")
        self.assertTrue(True)

    def test_payByDebit(self):
        print("Pay by debit")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()