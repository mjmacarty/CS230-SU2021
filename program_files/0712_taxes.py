# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:59:54 2021

@author: MattMacarty
"""

TAX_RATE = .2
STANDARD_DEDUCTION = 12200
DEPENDENT_DEDUCTION = 2000

print("Welcome to EZ-does-it Tax Calculator")

print("Enter your income: ")
income = float(input())

dependents = int(input("Enter number of dependents: "))

taxable_income = income - dependents * DEPENDENT_DEDUCTION - STANDARD_DEDUCTION
income_tax = taxable_income * TAX_RATE
effective_tax_rate = income_tax / income

print("=" * 25)
print("Taxable income: $ %.2f" % taxable_income)
print("Income Tax Due: $ %.2f" % income_tax)
print("Income Tax Due: $ " + str(income_tax))
print("Income Tax Due: $ {:,.2f}".format(income_tax))
# helpful for homework formatting output
print(f"Income Tax Due: $ {income_tax:15,.2f}")
print(f"Effective tax rate: {effective_tax_rate:14.2%}")











