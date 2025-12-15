# bounce.py
#
# Exercise 1.5
height = 100
number = 1

while number <= 10:
    height = height * 3 / 5
    print(number, round(height, 4))
    number += 1
