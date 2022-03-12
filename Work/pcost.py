# pcost.py with csv module
import csv, sys
import enum

def portfolio_cost(filename):

    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
            except ValueError as e:
                print(f'Row {rowno}: Bad row: {row}, error {e}')
            
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