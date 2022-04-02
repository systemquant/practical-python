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

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)

    print('Total cost', cost)
