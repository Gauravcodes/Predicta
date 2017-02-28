import pymongo

client = pymongo.MongoClient()
db = client.test
sports = db.sports.find()
sprts[i] = sports['value']
print(sprts)
for sport in sports:
     print(sport)