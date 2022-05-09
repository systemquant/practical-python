class Stock:
    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name: str = name
        self.shares: int = shares
        self.price: float = price

    def __repr__(self) -> str:
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('expected an integer')
        self._shares = value

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, nshares: int):
        self.shares -= nshares

        # return nshares * self.price


if __name__ == '__main__':
    goog = Stock('GOOG', 100, 490.1)
    print(repr(goog))

    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')
    print(portfolio)

    print(goog.cost)
    # goog.shares = '10'
