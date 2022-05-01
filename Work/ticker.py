from follow import follow
import csv
import report
import tableformat

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines, names):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    #rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    rows = filter_symbols(rows, names)

    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name', 'price', 'change'])

    for row in parse_stock_data(lines, portfolio):
        rowdata = [row['name'], row['price'], row['change']]
        formatter.row(rowdata)


if __name__ == '__main__':
    # lines = follow('Data/stocklog.csv')
    
    # for row in parse_stock_data(lines):
    #     print(row)

    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')