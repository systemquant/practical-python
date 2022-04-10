from stock import Stock


class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    def cost(self):
        return self.factor * super().cost()


if __name__ == '__main__':
    s = MyStock('GOOG', 100, 490.1, 2)

    print(s.cost())
    s.sell(25)
    print(s.shares)
    print(s.cost())
    s.panic()
    print(s.shares)

