import stock

a = stock.Stock('GOOG', 100, 490.10)
print(a.name)
print(a.shares)
print(a.price)

b = stock.Stock('AAPL', 50, 122.34)
c = stock.Stock('IBM', 75, 91.75)
print(b.shares * b.price)