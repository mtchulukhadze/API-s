from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "data": {
            "name": "mikheil"
        }
    }

@app.get("/about")
def about():
    return {
        "about": {
            "info": "page"
        }
    }

@app.get("/home")
def home():
    return {
        "home": {
            "name": "home"
        }
    }