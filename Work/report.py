# report.py
#
# Exercise 2.4

import csv
from pprint import pprint


def read_portfolio(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            # holding = ( row[0], int(row[1]), float(row[2]) )
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)

        return portfolio


def read_prices(filename):
    prices = {}
    f = open("Data/prices.csv", "r")
    rows = csv.reader(f)
    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except:
            pass

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


if __name__ == "__main__":
    """
    portfolio = read_portfolio('Data/portfolio.csv')

    #print(portfolio)
    pprint(portfolio)

    print(portfolio[1], portfolio[1]['shares'], sep='\n')
    total = 0.0
    for s in portfolio:
        total += s['shares'] * s['price']

    print(total)

    # Prices
    prices = read_prices('Data/prices.csv')
    pprint(prices)
    """

    portfolio = read_portfolio("Data/portfolio.csv")
    prices = read_prices("Data/prices.csv")

    report = make_report(portfolio, prices)

    headers = ("Name", "Shares", "Price", "Change")
    for i in headers:
        print(f"{i:>10s}", end=" ")
    print('')

    print(("-" * 10 + " ") * 4)

    for name, shares, price, change in report:
        price = round(price, 2)
        price_str = "$" + str(price)

        print(f'{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}')


"""    
    money = 0.0 # 자산
    profit = 0.0 # 손익
    total_cost = 0.0 # 평단가

    for dict in portfolio:
        #print(dict)

        name = dict['name']

        profit_indiv = prices[name] * dict['shares'] - dict['price'] * dict['shares']
        profit += profit_indiv
        total_cost += dict['price'] * dict['shares']

        print(f'{name} 잔고 손익: {profit_indiv}')

        money += prices[name] * dict['shares']

    print('')    
    print(f'현재 잔고 : {money}, 현재 손익 : {profit}, 평단가 : {total_cost}, 손익 비율 : {profit / total_cost * 100}%')
"""
