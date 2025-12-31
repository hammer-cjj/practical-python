# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    return parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])


def read_portfolio2(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # holding = {'name': row[0], 'shares': int(
            #     row[1]), 'price': float(row[2])}
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
    return portfolio


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    return dict(parse_csv(filename, types=[str, float], has_headers=False))


def read_prices2(filename):
    with open(filename, 'r') as f:
        prices = {}
        rows = csv.reader(f)
        for row in rows:
            if row:
                name = row[0]
                price = float(row[1])
                prices[name] = price
        return prices


def make_report(stocks, prices):
    report = []
    for stock in stocks:
        current_price = prices[stock['name']]
        change = current_price - float(stock['price'])
        summary = (stock['name'], stock['shares'], current_price, change)
        report.append(summary)
    return report


def print_report(report):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * 4)
    for name, shares, price, change in report:
        price = '$' + str(round(price, 2))
        shares = int(shares)
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

# files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
# for name in files:
#     print(f'{name:-^43s}')
#     portfolio_report(name, 'Data/prices.csv')
#     print()
