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
# run this: curl https://gist.githubusercontent.com/nmagee/8af7b3f71bbd14730f83bf365c20d878/raw/673ba528f4b9352eded70ddd131a319de02f2545/install.sh | bash
collection = db.jsondocs
directory = "."

complete_imported = 0
complete_notimported = 0
corrupted = 0
for filename in os.listdir(directory):
  with open(os.path.join(directory, filename)) as f:
    try:
        file_data = json.load(f)
    except Exception as e:
        print(f'exception: {e}')
        for docs in f:
            try:
                non_corrupted_files = json.load(docs) 
                complete_nonimported +=1
            except Exception as e:
                corrupted+=1
                print(e)
                continue
    continue
    if isinstance(file_data, list):
        collection.insert_many(file_data)
        for import_docs in file_data:
            complete_imported+=1
    else:
        collection.insert_one(file_data)
        complete_imported+=1
#print(complete_imported)

print(f'complete imported{complete_imported}')
print(f'complete not imported {complete_notimported}')
print(f'corrupted {corrupted}')