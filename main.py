import pymongo

client = pymongo.MongoClient('mongodb://172.31.43.47:27017,1172.31.36.137:27017,172.31.38.21:27017/?replicaSet=rs0')
db = client["chat_db"]
collection = db["chat"]
alias = input('Write your alias: ')

for i in collection.find():
  print(i["name"]+": "+i["msg"])

while True:
  msg = input('new message: ')

  mydict = { "name": alias, "msg": msg}
  a = collection.insert_one(mydict)

  print('Welcome to chat!')
  for i in collection.find():
    print(i["name"]+": "+i["msg"])
  print('---')