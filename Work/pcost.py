# pcost.py
import sys
import csv
import report

# Exercise 1.33


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return sum([float(item['price']) * int(item['shares']) for item in portfolio])


def portfolio_cost2(filename):
    total = 0.0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total += nshares * price
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    f.close()
    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

# cost = portfolio_cost(filename)
# print('Total cost:', cost)
