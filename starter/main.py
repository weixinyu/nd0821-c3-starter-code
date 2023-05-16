# Put the code for your API here.
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
# Instantiate the app.
app = FastAPI()

class Value(BaseModel):
    value: int
    
# Define a GET on the specified endpoint.
@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}

# Use POST action to send data to the server
@app.post("/{path}")
async def exercise_function(path: int, query: int, body: Value):
    return {"path": path, "query": query, "body": body}