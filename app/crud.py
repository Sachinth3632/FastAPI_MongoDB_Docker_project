from app.database import collection
from bson.objectid import ObjectId
from datetime import datetime

def create_inspection(data):
	data["timestamp"] = datetime.utcnow()
	data["is_active"] = True
	result = collection.insert_one(data)
	return result

def get_all_inspections(limit, offset):
	return list(collection.find({"is_active":True}).skip(offset).limit(limit))

def get_inspection(id):
	return collection.find_one({"_id": ObjectId(id)})

def update_inspection(id, data):
	return collection.update_one({"_id":ObjectId(id)}, {"$set": data})

def delete_inspection(id):
	return collection.update_one({"_id":ObjectId(id)}, {"$set" : {"is_active": False}})
