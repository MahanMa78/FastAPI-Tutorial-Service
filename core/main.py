from fastapi import FastAPI
# import uvicorn
import random
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


@app.get("/names/{name_id}")
def retrieve_name_detail(name_id:int):
    for name in names_list:
        if name["id"] == name_id:
            return name
    
    return {"detail" : "object not found    "}


@app.post("/names")
def create_name(name:str):
    
    name_obj = {"id" : random.randint(6,101) , "name" : name}
    names_list.append(name_obj)
    
    return name_obj



@app.put("/names/{name_id}")
def update_name_detail(name_id:int , name:str):
    for item in names_list:
        if item["id"] == name_id:
            item['name'] = name
            return item
        
    return {"detail" : "object not found"}