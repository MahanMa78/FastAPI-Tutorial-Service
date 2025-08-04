from fastapi import FastAPI
# import uvicorn

app = FastAPI()


names_list = [
    {"id" : 1 , "name": "mahan"},
    {"id" : 2 , "name": "homa"},
    {"id" : 3 , "name": "shayan"},
    {"id" : 4 , "name": "ali"},
    {"id" : 5 , "name": "aziz"},
]


@app.get('/')
def root():
    return {"message" : "Hello, World!"}


# *
# if __name__ == "__main__":
#     uvicorn.run( "main.app" , host="0.0.0.0" , port = "8000" , reload=True )
# * for running the server : uvicorn main.app --reload --host 0.0.0.0 --port 8000




@app.get("/names")
def retrieve_names_list():
    return names_list