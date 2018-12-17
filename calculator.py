#!/usr/bin/env python3

import sys

def getInfo(infos):
    dic = {}
    for i in infos:
        lis = i.split(':')
        dic[lis[0]] = lis[1]

    return dic


def afterSalary(salary):
    tax = salary * 0.08 + salary * 0.02 + salary * 0.005 + salary * 0.06 
    tax_amount = salary - tax - 3500
     
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
    
    return salary - tax - amount


if __name__ == '__main__':

    infos = getInfo(sys.argv[1:])
    
    for uid,salary in infos.items():
        try:
            print(int(uid),':',format(afterSalary(int(salary)),'.2f'))
        except:
            print('Parameter Error')
