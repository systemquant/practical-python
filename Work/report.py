# report.py
#
# Exercise 2.4

#import csv
import fileparse
import sys

def read_portfolio(filename):
    portfolio = fileparse.read_csv(
        filename, select=['name', 'shares', 'price'], types=[str, int, float])

    return portfolio


def read_prices(filename):
    prices = dict(fileparse.read_csv(
        filename, types=[str, float], has_headers=False))

    return prices


def make_report(portfolio, prices):
    report = []

    # print(f'{"Name":>10s}  {"Shares":>10s}  {"Price":>10s}  {"Change":>10s}')

    for dict in portfolio:
        name = dict["name"]
        shares = dict["shares"]
        now_price = prices[name]

        profit_indiv = now_price * shares - dict["price"] * shares
        # profit += profit_indiv
        # total_cost += dict['price'] * shares

        change = now_price - dict["price"]

        # print(f'{name} 잔고 손익: {profit_indiv}')

        # money += prices[name] * shares

        report.append((name, shares, prices[name], change))

    return report


def print_report(report):
    headers = ("Name", "Shares", "Price", "Change")
    for i in headers:
        print(f"{i:>10s}", end=" ")
    print("")

    print(("-" * 10 + " ") * len(headers))

    for name, shares, price, change in report:
        price = round(price, 2)
        price_str = "$" + str(price)

        print(f"{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv: list):
    if len(argv) == 1:
        portfolio_report("Data/portfolio.csv", "Data/prices.csv")
    elif len(argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
    else:
        portfolio_report(argv[1], argv[2])


if __name__ == "__main__":
    main(sys.argv)
