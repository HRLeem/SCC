from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

# sival = list(db.movies.find_one({'title':'어벤져스: 엔드게임'}))
# print(sival['star'])

target_movie = db.movies.find_one({'title':'어벤져스: 엔드게임'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))

for movie in movies:
    db.movies.update({'title':movie['title']},{'$set':{'star':0}})
    print(movie['title'])

# print(target_star)