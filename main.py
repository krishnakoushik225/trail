from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client =  MongoClient('mongodb+srv://koushik0825:krishna2002@cluster0.vo0qr.mongodb.net/cab?retryWrites=true&w=majority')

@app.get("/")
async def root():
    return {"message": "Hello World"}

# create route to register a new user
@app.post("/register")
async def register(user: dict):
    print("connected to mongodb")
    # connect to mongoDB
    db = client.users

    # check if user already exists
    print(user)
    if db.users.find_one({"Email": user["Email"]}) is None:
        # insert user into database
        db.users.insert_one(user)
        return {"message": "User successfully registered"}
    else:
        return {"message": "User already exists"}

@app.post("/login")
async def login(user:dict):
    db = client.users
    if db.find_one({"Email": user["Email"]}) is None:
        return {"message": "User not found"}
    else:
        if db.find_one({"Email": user["Email"], "password": user["password"]}) is None:
            return {"message": "Password incorrect"}
        else:
            return {"message": "Login successful"}