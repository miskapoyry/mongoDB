from pymongo import MongoClient;

client = MongoClient("mongodb://localhost:27017/")
db = client["project"]

# Here are the collections
teams_collection = db["teams"]
matches_collection = db["matches"]