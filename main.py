from typing import Union
from pydantic import BaseModel, PositiveInt # This is to be used for data validation
from fastapi import FastAPI

# Create a rest server
app = FastAPI()

# Creating a home route
@app.get("/")
def home():
    return "This Works!" # To return something in the response use the return statement





