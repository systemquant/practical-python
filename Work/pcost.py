# pcost.py
import sys
import report


def portfolio_cost(filename):

    total_cost = 0.0
    portfolio = report.read_portfolio(filename)

    for rowno, record in enumerate(portfolio):
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
        except ValueError as e:
            print(f'Row {rowno}: Bad line: {record}, error {e}')

        else:
            total_cost += nshares * price

    return total_cost


def main(argv: list):
    if len(argv) == 1:
        filename = 'Data/portfolio.csv'
    elif len(argv) == 2:
        filename = argv[1]
    else:
        raise SystemExit(f'Usage: {sys.argv[0]} portfile')

    cost = portfolio_cost(filename)

    print('Total cost', cost)


if __name__ == '__main__':
    main(sys.argv)
