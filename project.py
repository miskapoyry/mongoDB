from pymongo import MongoClient;

client = MongoClient("mongodb://localhost:27017/")
# Change "library" to match the name of your database
db = client["project"]
# Change the collection name to match the name of your collection
teams = db.teams.find()

for team in teams:
  # Documents are generally turned into dictionaries in which there's a key for each field
  # The following code prints the value of the "title" field
  print(team["name"])
  # Try printing all the fields of a document