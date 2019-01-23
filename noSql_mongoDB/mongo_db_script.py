# -*- coding: utf-8 -*-
from pymongo import MongoClient, errors


expdate = input("What is the date of the expense?\n\n(use date format yyyy-mm-dd)\n\nData is:")
vender = input("Who is the vender?")
value = input("What is the value of the expense?")
value = float(value)
category = input("What is the category of the expense?\n\nOptions are:\n\nBar/Rest\nCoworkers\nExtra\nGas\nGroceries\n\nCategory is:")

"""
creating a database and collection inside
mongodb.  Note: dbs and collections aren't
created until you write a documents into them
"""
try:
    client = MongoClient('localhost')
except errors.ConnectionFailure as e:
        print("Connection error")

try:
    db = client['jeremys_expenses']
    coll = db['expenses']
    expenseDict = {"Date":expdate,"vender":vender,"value":value,"category":category}
    x = coll.insert_one(expenseDict)
except errors.PyMongoError as e:
        print(e)

myquery = coll.find()

for i in myquery:
    print(i)

"""
run the below script to delete all documents out of
the mongodb collection.....CAREFUL!
"""
"""
delDocs = coll.delete_many({})
print(delDocs.deleted_count, "documents deleted")
"""
