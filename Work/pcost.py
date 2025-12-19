# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    total = 0.0
    for line in f:
        line_list = line.split(',')
        total += int(line_list[1]) * float(line_list[2][:-1])
    print('Total cost', total)
