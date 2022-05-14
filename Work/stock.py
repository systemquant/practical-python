from typedproperty import typedproperty

String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)


class Stock:
    __slots__ = ('_name', '_shares', '_price')
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name: str = name
        self.shares: int = shares
        self.price: float = price

    def __repr__(self) -> str:
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

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
