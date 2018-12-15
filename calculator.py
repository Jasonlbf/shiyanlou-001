#!/usr/bin/env python3

import sys

salary = 0
try:
    salary = int(sys.argv[1])
except:
    print('Parameter Error')
    exit()

tax_amount = salary - 3500

if tax_amount <= 0:
    amount = 0
elif tax_amount <= 1500:
    amount = tax_amount * 0.03
elif tax_amount <= 4500:
    amount = tax_amount * 0.1 - 105
elif tax_amount <= 9000:
    amount = tax_amount * 0.2 - 555
elif tax_amount <= 935000:
    amount = tax_amount * 0.25 - 1005
elif tax_amount <= 55000:
    amount = tax_amount * 0.3 - 2755
elif tax_amount <= 80000:
    amount = tax_amount * 0.35 - 5505
else:
    amount = tax_amount * 0.45 - 13505

print(format(amount,'.2f'))
