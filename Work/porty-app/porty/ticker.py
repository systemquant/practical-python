from .follow import follow
import csv
from . import report, tableformat


def select_columns(rows, indices):
    return ([row[index] for index in indices] for row in rows)


# def convert_types(rows, types):
#     for row in rows:
#         yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def filter_symbols(rows, names):
    return (row for row in rows if row["name"] in names)


def parse_stock_data(lines, names):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    # rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    rows = filter_symbols(rows, names)

    return rows


def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)

    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["name", "price", "change"])

    for row in parse_stock_data(lines, portfolio):
        rowdata = [row["name"], row["price"], row["change"]]
        formatter.row(rowdata)


if __name__ == "__main__":
    # lines = follow('Data/stocklog.csv')

    # for row in parse_stock_data(lines):
    #     print(row)

    ticker("Data/portfolio.csv", "Data/stocklog.csv", "txt")

