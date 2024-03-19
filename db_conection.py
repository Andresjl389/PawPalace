import pymongo

# url = 'mongodb+srv://Andreses:XGVkDlAyN5Bp3N8x@cluster0.eydrwxt.mongodb.net/'
url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)

db = client['second_test']