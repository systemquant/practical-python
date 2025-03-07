# pcost.py
from . import report


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)

    return portfolio.total_cost


def main(argv: list):
    if len(argv) == 1:
        filename = 'Data/portfolio.csv'
    elif len(argv) == 2:
        filename = argv[1]
    else:
        raise SystemExit(f'Usage: {argv[0]} portfile')

    cost = portfolio_cost(filename)

    print('Total cost', cost)


if __name__ == '__main__':
    import sys

    main(sys.argv)
