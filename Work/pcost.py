# pcost.py
#
# Exercise 1.27
# with open('Data/portfolio.csv', 'rt') as f:
#     next(f)
#     total = 0.0
#     for line in f:
#         line_list = line.split(',')
#         total += int(line_list[1]) * float(line_list[2][:-1])
#     print('Total cost', total)

# Exercise 1.30
def portfolio_cost(filename):
    total = 0.0
    with open('Data/portfolio.csv', 'rt') as f:
        next(f)
        for line in f:
            line_list = line.split(',')
            total += int(line_list[1]) * float(line_list[2][:-1])
    return total


cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
