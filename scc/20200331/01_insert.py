from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

db.users.insert_one({'nama':'bobby', 'age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})