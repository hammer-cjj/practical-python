# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
pay_month = 0

while principal > 0:
    pay_month += 1

    if principal * (1 + rate / 12) > payment:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    else:
        total_paid = total_paid + principal * (1 + rate / 12)
        principal = 0

    if pay_month >= extra_payment_start_month and pay_month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(f'{pay_month} {total_paid: 0.2f} {principal: 0.2f}')

print(f'Total paid {total_paid: 0.2f}')
print(f'Months {pay_month}')
