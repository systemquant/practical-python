from . import stock, fileparse


class Portfolio:
    def __init__(self):
        self._holdings = []

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __str__(self):
        return self._holdings.__str__()

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)

    @classmethod
    def from_csv(cls, filename, **opts):
        self = cls()
        with open(filename, 'r') as lines:
            portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float], **opts)

            for d in portdicts:
                try:
                    self.append(stock.Stock(**d))
                except TypeError as e:
                    pass

        return self

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares

        return total_shares
