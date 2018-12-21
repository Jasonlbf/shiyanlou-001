#!/usr/bin/env python3

import sys
import csv

class Utils():
    @staticmethod
    def config(config):
        info = {}
        with open(config) as f:
            for line in f:
                line_s = line.split(' = ')
                info[line_s[0]] = float(line_s[1].rstrip())
        return info


class Args():
    @staticmethod
    def get_filepath(tag):
        if tag in ('-c','-d','-o'):
            args = sys.argv[1:]
            return args[args.index(tag)+1]
        else:
            print("please use -d -c -o parameter")


class UserData():
    def __init__(self,userdata):
        self._userdata = userdata
    @property
    def userdata(self):
        userinfo = {}
        with open(self._userdata) as f:
            for line in f:
                line_s = line.split(',')
                userinfo[line_s[0]] = int(line_s[1])
            return userinfo

class IncomeTaxCalculater():
    def __init__(self,config,filepath,userdata):
        self.config = config
        self.filepath = filepath
        self.userdata = userdata

    def salary_info(self,uid,salary):
        salary_info = {}
        tax = 0
        jishuL = self.config['JiShuL']
        jishuH = self.config['JiShuH']
        if salary < jishuL: 
            tax = jishuL * 0.08 + jishuL * 0.02 + jishuL * 0.005 + jishuL * 0.06 
        elif salary > jishuH:
            tax = jishuH * 0.08 + jishuH * 0.02 + jishuH * 0.005 + jishuH * 0.06 
        else:
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
        
        after_salary = salary - tax - amount
        salary_info = [uid,salary, '%.2f' % tax, '%.2f' % amount, '%.2f' % after_salary]
        return salary_info 

    def export(self):
        with open(self.filepath,'w') as f:
            
            for uid,salary in self.userdata.items():
                salary_info = self.salary_info(uid,salary)
                csv.writer(f).writerow(salary_info)

if __name__ == '__main__':
    config = Utils.config(Args.get_filepath('-c'))
    userfile = Args.get_filepath('-d')
    outfile = Args.get_filepath('-o')

    userinfo = UserData(userfile)
    taxcal = IncomeTaxCalculater(config,outfile,userinfo.userdata)
    taxcal.export()
