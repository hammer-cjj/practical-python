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


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total = 0.0
for s in portfolio:
    total += s['shares'] * (prices[s['name']] - s['price'])
print(total)
