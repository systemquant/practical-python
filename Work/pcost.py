# pcost.py with csv module
import csv, sys

def portfolio_cost(filename):

    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        headers = next(rows)

        for row in rows:
            try:
                nshares = int(row[1])
            
            except Exception as e:
                print("Seems to be shares missing: ", e)
            
            else:
                price = float(row[2])
                total_cost += nshares * price

        return total_cost

                



if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    
    cost = portfolio_cost(filename)

    print('Total cost', cost)