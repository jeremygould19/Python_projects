# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pymysql
from pymongo import MongoClient, errors

class Expenses(object):

    def __init__(self,host_address,username,password,database):
        try:
            print("connecting to mysql...")
            self._db_connection = pymysql.connect(host=host_address,  user=username, passwd=password,db=database)
            self._db_cur = self._db_connection.cursor()
            print("mysql connection success!\nConnecting to mongodb next...")
            self.mongoclient=MongoClient('localhost')
            print("mongodb connection success!")
        except Exception as e:
            print('Got error {}, errno is {}'.format(e, e.args[0]))

    def expense_add(self):

        expdate = input("What is the date of the past expense?\n\n(use date format yyyy-mm-dd)\n\nDate is:")
        vender = input("Who is the vender?")
        value = input("What is the value of the past expense?")
        value = float(value)
        category = input("What is the category of the past expense?\n\nOptions are:\n\nBar/Rest\nCoworkers\nExtra\nGas\nGroceries\nVenmo\n\nCategory is:")


        try:
            db = self.mongoclient['jeremys_expenses']
            coll = db['expenses']
            expenseDict = {"Date":expdate,"vender":vender,"value":value,"category":category}
            coll.insert_one(expenseDict)
            print('record ', expenseDict, ' successfully written to mongodb')
        except errors.PyMongoError as e:
                print(e)

        sql = "INSERT INTO JEREMYS_EXPENSES (date,category,cost,vender) VALUES (%s,%s,%s,%s)"
        val=(expdate,category,value,vender)
        try:
            self._db_cur.execute(sql,val)
            self._db_connection.commit()
        finally:
            print("mySql insert success:", sql, "with", val)

    def expense_summary(self):
        sql = "SELECT Category, SUM(cost) as last_week_cost \
                FROM JEREMYS_EXPENSES \
                WHERE `date` >= DATE_SUB(NOW(), INTERVAL 28 day) AND `date` <= NOW() \
                GROUP BY category;"
        try:
            self._db_cur.execute(sql)
        finally:
            result = self._db_cur.fetchall()
            print('Monthly budget is Gas:60, Extra:580, Coworkers:200, Groceries:400, Bar/Rest:500\nTotal:1740\n\nTotal monthly costs:\n')
            costs = []
            for a,b in result:
                print(a,'spend:',b)
                if a == 'Gas':
                    print('Weekly Gas $ left: ', 60 - b, '\n')
                elif a == 'Extra':
                    print('Weekly Extra $ left: ',580 - b, '\n')
                elif a == 'Coworkers':
                    print('Weekly Coworkers $ left: ',200 - b, '\n')
                elif a == 'Groceries':
                    print('Weekly Groceries $ left: ',400 - b, '\n')
                elif a == 'Bar/Rest':
                    print('Weekly Bar/Rest $ left: ',500 - b, '\n')
                else:
                    print('\n')
                costs.append(b)
                print('Total monthly spend is: ',sum(costs),'\nTotal left: ',1740-sum(costs),'\n')

            sql = "SELECT category, SUM(cost) as last_week_cost \
                    FROM (SELECT category, cost, date, WEEKDAY(date) as dayindex \
                    FROM JEREMYS_EXPENSES \
                    WHERE WEEKDAY(date) <= WEEKDAY(CURDATE()) \
                    AND `date` >= DATE_SUB(NOW(), INTERVAL 7 day) AND `date` <= NOW()) as LastMonday \
                    GROUP BY category;"

        try:
            self._db_cur.execute(sql)
        finally:
            result = self._db_cur.fetchall()
            print('\nWeekly budget is Extra = 145, Coworkers = 50, Gas = 15, Groceries = 100, Bar/Rest = 125\nTotal:435\n\nCosts since Monday are:\n')
            weeklycostlist = []
            for a,b in result:
                print(a, 'spend:',b)
                if a == 'Gas':
                    print('Weekly Gas $ left: ', 15 - b, '\n')
                elif a == 'Extra':
                    print('Weekly Extra $ left: ',145 - b, '\n')
                elif a == 'Coworkers':
                    print('Weekly Coworkers $ left: ',50 - b, '\n')
                elif a == 'Groceries':
                    print('Weekly Groceries $ left: ',100 - b, '\n')
                elif a == 'Bar/Rest':
                    print('Weekly Bar/Rest $ left: ',125 - b, '\n')
                else:
                    print('\n')
                weeklycostlist.append(b)
            print('Total: ',sum(weeklycostlist),'\nTotal $ left: ',435-sum(weeklycostlist))

    def future_expense(self):

        future_expdate = input("What is the date of the future expense?\n\n(use date format yyyy-mm-dd)\n\nDate is:")
        value = input("What is the value of the future expense?")
        value = float(value)
        description = input("Describe the future expense?")

        try:
            db = self.mongoclient['jeremys_expenses']
            coll = db['expenses']
            expenseDict = {"future_expense_date":future_expdate,"cost":value,"description":description}
            coll.insert_one(expenseDict)
            print('record ', expenseDict, ' successfully written to mongodb')
        except errors.PyMongoError as e:
            print(e)

        sql = "INSERT INTO future_expenses (date,cost,description) VALUES (%s,%s,%s)"
        val=(future_expdate,value,description)

        try:
            self._db_cur.execute(sql,val)
            self._db_connection.commit()
        finally:
            print("mySql insert success:", sql, "with", val)

    def __del__(self):
        self._db_connection.close()
        self.mongoclient.close()
        print("connection closed")
