from copy import deepcopy
import unittest
import stock


class TestStock(unittest.TestCase):

    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        
        self.assertEqual(s.cost, 49010.0)

        shares_ = deepcopy(s.shares)
        sell_amount = 20
        s.sell(sell_amount)
        self.assertEqual(s.shares, shares_ - sell_amount)

        #self.assertIsInstance(s.shares, int)

    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '100'


if __name__ == '__main__':
    unittest.main()