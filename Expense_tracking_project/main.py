# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

os.chdir('/Users/jeremygould/Documents/OpenSourceWork/Expense_py_app/Expense_app_v2')

import pkg.Expense_funcs as Ex

exp = Ex.Expenses(<host ip address>,<user name>,<password>,<db name>)

status = 0

while status == 0:
    task = input("\nWhat would you like to do?\n\nSubmit a new past expense: 1\nSubmit a future expense: 2\nRun an expense report: 3\n")

    if task == '1':
        exp.expense_add()

    elif task == '2':
        exp.future_expense()

    else:
        exp.expense_summary()

    nextStep = input("Is there something else you'd like to do (y/n)?")
    if nextStep == "y" or nextStep == "Y":
        pass
    else:
        print("Thanks for playing! Goodbye.")
        status = 1
