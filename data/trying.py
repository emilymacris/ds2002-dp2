#!/home/gitpod/.pyenv/shims/python3

import pymongo
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.bdf7bz
# specify a collection
collection = db.jsondocs

path = "."

complete_imported = 0
complete_notimported = 0
corrupted = 0
for (root, dirs, files) in os.walk(path):
    for f in files:
        with open(f) as file1:
            try:
                file_data = json.load(file1)
                if isinstance(file_data, list):
                    collection.insert_many(file_data)  
                    complete_imported+=1
                else:
                    collection.insert_one(file_data)
                    complete_imported+=1
                
        # if the whole file doesn't load, what do you do?   - this is just counting   
            except Exception as e:
                for docs in file1:
                    try:
                        corrupted = json.load(docs) 
                        complete_nonimported +=0 
                    except Exception as e:
                        corrupted+=1
                        continue
print(complete_imported, "|", complete_notimported, "|", corrupted)
            # for docs in file1:
            #     print(type(docs))

            # try:
            #     file_data = json.load(file1)
            #         for docs in file_data:

            # try:
            #     file_data = json.load(file1)

            # except Exception as e:
            #     for docs in file1:

          
            #print(file_data)
           # for docs in file_data[0:1]:
             #   print(json.dumps(docs, indent=4))
         #   print(json.dumps(file_data, indent=4))