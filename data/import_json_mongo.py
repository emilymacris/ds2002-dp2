#!/home/gitpod/.pyenv/shims/python3

import pymongo
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

#remember to use MONGO-ATLAS to connect to shell

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.bdf7bz
# specify a collection
collection = db.jsondocs


# return RECORDS IMPORTED OK
# GOOD RECORDS NOT IMPORTED - like if one in file ?
# how many records were corrupted 
# 


path = "."

for (root, dirs, file) in os.walk(path):
    for f in file:
        with open(f) as file:
            try:
                file_data = json.load(file)
            except Exception as e:
                print(file, "has an error", e)
                continue
            if isinstance(file_data, list):
                collection.insert_many(file_data)  
            else:
                collection.insert_one(file_data)



# assuming you have defined a connection to your db and collection already:


     
# Inserting the loaded data in the collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used




# import pymongo
# from pymongo import MongoClient, errors
# from bson.json_util import dumps
# import os
# import json

# MONGOPASS = os.getenv('MONGOPASS')
# uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
# client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# # specify a database
# db = client.bdf7bz
# # specify a collection
# collection = db.json-data

