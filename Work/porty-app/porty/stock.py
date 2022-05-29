from .typedproperty import String, Integer, Float


class Stock:
    __slots__ = ('_name', '_shares', '_price')
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, nshares: int):
        self.shares -= nshares

        # return nshares * self.price
