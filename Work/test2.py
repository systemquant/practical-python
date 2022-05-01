def custom_iter(obj):
    _iter = obj.__iter__()
    while True:
        try:
            print(_iter.__next__(), end='')
        except StopIteration:
            break

with open("Data/portfolio.csv") as f:
    custom_iter(f)

