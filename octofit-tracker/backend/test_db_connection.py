from pymongo import MongoClient

# Test MongoDB connection
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Insert test data
db.test_collection.insert_one({"test_key": "test_value"})

# Retrieve test data
result = db.test_collection.find_one({"test_key": "test_value"})
print("Test data retrieved from MongoDB:", result)

# Clean up
db.test_collection.drop()