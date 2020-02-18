import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.wordbook
word_table = db.words
user_table = db.users