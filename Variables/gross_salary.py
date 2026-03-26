"""
Gross Salary Calculator
Given basic salary, calculate:

HRA = 20% of basic

DA = 50% of basic

Gross salary = Basic + HRA + DA
"""

def salary(basic_salary):
    hra = 0.2*basic_salary
    da = 0.5*basic_salary
    gross_salary = basic_salary + hra + da
    return gross_salary

print(salary(20000))

