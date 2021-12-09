# Program to test the NoSQL MongoDB

from pymongo import MongoClient
import datetime


conn = MongoClient('localhost', 27017)
db = conn.cadastrodb
collection = db.cadastrodb

dict1 = {'código': 'ID-9987725', \
        'prodNome': 'Geladeira', \
        'marcas': ['brastemp', 'consul', 'electrolux'], \
        'dataCadastro': datetime.datetime.utcnow()}

collection = db.dictionaries

post_id = collection.insert_one(dict1)

post_id.inserted_id

dict2 = {'código': 'ID-2209876', \
        'prodNome': 'Televisor', \
        'marcas': ['samsung', 'panasonic', 'lg'], \
        'dataCadastro': datetime.datetime.utcnow()}

collection = db.dictionaries

post_id = collection.insert_one(dict2).inserted_id

'''for post in collection.find():
    print(post)'''

print(db.name)
print(db.collection_names())
