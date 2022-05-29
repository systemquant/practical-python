# report.py

# import csv
import sys
from . import stock, fileparse, tableformat
from .portfolio import Portfolio


def read_portfolio(filename, **opts):
    """
    주식 포트폴리오 파일을 읽어 딕셔너리의 리스트를 생성.
    name, shares, price를 키로 사용.
    """

    return Portfolio.from_csv(filename, **opts)


def read_prices(filename):
    prices = dict(fileparse.read_csv(filename, types=[str, float], has_headers=False))

    return prices


def make_report_data(portfolio, prices):
    report = []

    for stock in portfolio:
        name = stock.name
        shares = stock.shares
        now_price = prices[name]

        profit_indiv = now_price * shares - stock.price * shares

        change = now_price - stock.price
        summary = (name, shares, prices[name], change)
        report.append(summary)

    return report


def print_report(reportdata, formatter):
    """
    (name, shares, price, change) 튜플의 리스트로부터 보기 좋게 포매팅한 테이블을 프린팅.
    """

    formatter.headings(['Name', 'Shares', 'Price', 'Change'])

    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    """
    주어진 포트폴리오와 가격 데이터 파일을 가지고 주식 보고서를 작성.
    """
    # 데이터 파일 읽기
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # 보고서 데이터 생성
    report = make_report_data(portfolio, prices)

    # 프린트
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv: list):
    if len(argv) == 1:
        portfolio_report('Data/portfolio.csv', 'Data/prices.csv', 'txt')

    elif len(argv) == 3:
        portfolio_report(argv[1], argv[2])

    elif len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])

    else:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')


if __name__ == '__main__':
    main(sys.argv)
