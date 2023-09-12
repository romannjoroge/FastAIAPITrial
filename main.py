from typing import Union
from pydantic import BaseModel, PositiveInt # This is to be used for data validation
from fastapi import FastAPI

# Create a rest server
app = FastAPI()

# Creating a home route
@app.get("/")
def home():
    return "This Works!" # To return something in the response use the return statement

# Defining route with query string
@app.get("/item/{item_name}")
def queryStringFunction(item_name: str):
    return f"The searched item is {item_name}"

# Defining route with named parameters
@app.get("/item")
def namedParameterFunction(age: Union[int, None], name: str):
    return f"{name} is {age} years old"

# Defining the structure of the POST JSON Body
class DetailsBody(BaseModel):
    name: str
    age: Union[PositiveInt, None] = 0
    occupation: Union[str, None] = "Computer Scientist" # Defining a value thats nullable and has a default value

# Defining a route that accepts a JSON body
@app.post("/details")
def detailsFunction(person: DetailsBody):
    return f"The person created is called {person.name}, is {person.age} years old and is a {person.occupation}"



