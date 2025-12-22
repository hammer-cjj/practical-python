# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(
                row[1]), 'price': float(row[2])}
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
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
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        report.append(summary)
    return report


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * 4)
for name, shares, price, change in report:
    price = '$' + str(round(price, 2))
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
