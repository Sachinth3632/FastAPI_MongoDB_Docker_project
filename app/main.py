from fastapi import FastAPI, HTTPException
from app.schemas import Inspection
from app import crud
from bson.objectid import ObjectId

app = FastAPI()

@app.post("/inspections")
def create_inspection(data: Inspection):
    result = crud.create_inspection(data.dict())
    return {"id": str(result.inserted_id)}

@app.get("/")
def root():
	return {"message": "API is running"}

@app.get("/inspections")
def get_all(limit: int = 10, offset: int = 0):
    data = crud.get_all_inspections(limit, offset)
    for d in data:
        d["_id"] = str(d["_id"])
    return data

@app.get("/inspections/{id}")
def get_one(id: str):
    data = crud.get_inspection(id)
    if not data:
       raise HTTPException(status_code=404, detail="Inspection not found")
    data["_id"] = str(data["_id"])
    return data

@app.put("/inspections/{id}")
def update(id: str, data: dict):
	crud.update_inspection(id,data)
	return {"message": "updated"}

@app.delete("/inspections/{id}")
def delete(id: str):
	crud.delete_inspection(id)
	return {"message": "soft deleted"}

@app.get("/inspections/stats")
def stats():
	total = crud.collection.count_documents({})
	active = crud.collection.count_documents({"is_active": True})
	return {
		"total": total,
		"active": active
	}

