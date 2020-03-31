from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find())

for user in all_users:
    name = user['name']
    age = user['age']
    print('name : ' , name , '   age : ' , age)

print('\n\n')

same_ages = list(db.users.find({'age':27}))

print(same_ages)

print('\n\n\n\n')

