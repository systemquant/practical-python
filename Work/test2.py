import report, fileparse

portfolio = fileparse.read_csv(
        'Data/portfolio.csv.gz', select=['name', 'shares', 'price'], types=[str, int, float])