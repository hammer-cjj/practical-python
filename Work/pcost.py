# pcost.py
import sys

# Exercise 1.33


def portfolio_cost(filename):
    total = 0.0
    with open(filename, 'rt') as f:
        next(f)

        for line in f:
            try:
                line_list = line.split(',')
                total += int(line_list[1]) * float(line_list[2][:-1])
            except ValueError:
                print('Bad row:', line)
    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
