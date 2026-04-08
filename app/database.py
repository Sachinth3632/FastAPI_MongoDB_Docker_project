from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client["inspection_db"]
collection = db["inspections"]
