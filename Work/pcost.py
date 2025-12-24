# pcost.py
import sys

# Exercise 1.33


def portfolio_cost(filename):
    total = 0.0
    with open(filename, 'rt') as f:
        next(f)

        for rowno, row in enumerate(f, start=1):
            try:
                row_list = row.split(',')
                total += int(row_list[1]) * float(row_list[2][:-1])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
