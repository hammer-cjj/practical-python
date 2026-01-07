#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
import stock
import tableformat


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as lines:
        lines_list = parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )
        return [
            stock.Stock(item["name"], item["shares"], item["price"])
            for item in lines_list
        ]


def read_portfolio2(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # holding = {'name': row[0], 'shares': int(
            #     row[1]), 'price': float(row[2])}
            record = dict(zip(headers, row))
            stock = {
                "name": record["name"],
                "shares": int(record["shares"]),
                "price": float(record["price"]),
            }
            portfolio.append(stock)
    return portfolio


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))


def read_prices2(filename):
    with open(filename, "r") as f:
        prices = {}
        rows = csv.reader(f)
        for row in rows:
            if row:
                name = row[0]
                price = float(row[1])
                prices[name] = price
        return prices


def make_report_data(stocks, prices):
    report = []
    for stock in stocks:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        report.append(summary)
    return report


def print_report(reportdata, formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    # print('%10s %10s %10s %10s' % headers)
    # print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)
        # price = '$' + str(round(price, 2))
        # shares = int(shares)
        # print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')


def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit(f"Usage: {args[0]} " "portfolio-file price-file format")
    portfolio_report(args[1], args[2], args[3])


if __name__ == "__main__":
    import sys

    main(sys.argv)
