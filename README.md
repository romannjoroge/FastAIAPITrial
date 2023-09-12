# FastAPI
This allows you to create an asynchronous REST API Server using python.

## Requirements
Install fastai
```bash
pip install fastai
```
Install a package that implements an ASGI server. An example is uvicorn.
```bash
pip install "uvicorn[standard]"
```

## Creating routes 
We can define the routes in a *main.py* file. 

### Defining routes
Routes in FastAI are functions that have the app.[method] decorator. The decorator defines the route and the function is ran when the route is hit. To return something in the response you return a value from the function.
```python
@app.get("/")
def home():
    return "Hello World"
```

### Defining routes with query strings
Routes with query strings are defined in the following manner. The name of the query parameter is kept in curly braces in the api path defined in the decorator. The parameter can then be accessed in the function by defining a function with an arguement that's the same name as the query parameter
```python
@app.get("/item/{item_name}")
def getItemDetailsFromName(string: item_name):
    return data[item_name]
```

### Defining routes with named parameters
To define a query with named parameters we do the following: In the function that handles the routes add an argument. The name of the arguement is the same as the name of the parameter
```python
@app.get("/item")
def getItemFromParameters(q: Union[str, none], a: str):
    # To define an optional parameter
    return {"q": q, "a": a}
```