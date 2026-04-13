# FastAPI_MongoDB_Docker_project

FastAPI server is running inside a Docker container
MongoDB is running in a separate Docker container
docker-compose.yml is used to orchestrate both services
All APIs are implemented and tested using Swagger/Postman
POST /inspections (Create inspection)
GET /inspections (Get all inspections)
GET /inspections/{id} (Get single inspection)
PUT /inspections/{id} (Update inspection)
DELETE /inspections/{id} (Soft delete inspection)
Proper error handling implemented:
422 Validation Error → for missing or invalid request body
400 Bad Request → for invalid ID format
404 Not Found → when inspection is not present in database
Data is stored in MongoDB and _id is converted to string in responses
Soft delete is implemented using is_active = False
Code is pushed to personal GitHub repository