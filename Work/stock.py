class Stock:

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name: str = name
        self.shares: int = shares
        self.price: float = price

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, nshares: int):
        self.shares -= nshares

        # return nshares * self.price
    
    