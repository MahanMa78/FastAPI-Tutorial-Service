from fastapi import FastAPI , Query
# import uvicorn
from typing import Annotated ,Optional
import random
app = FastAPI()


names_list = [
    {"id" : 1 , "name": "mahan"},
    {"id" : 2 , "name": "homa"},
    {"id" : 3 , "name": "shayan"},
    {"id" : 4 , "name": "ali"},
    {"id" : 5 , "name": "aziz"},
    {"id" : 6 , "name": "mahan"},
    {"id" : 7 , "name": "mahan"},
    {"id" : 8 , "name": "mahan"},
]


@app.get('/')
def root():
    return {"message" : "Hello, World!"}


# *
# if __name__ == "__main__":
#     uvicorn.run( "main.app" , host="0.0.0.0" , port = "8000" , reload=True )
# * for running the server : uvicorn main.app --reload --host 0.0.0.0 --port 8000




@app.get("/names")
def retrieve_names_list(q:str | None = Query(default=None , max_length=50)): 
    #model1 :: q:str | None = None---->in ghesmate None = None ro baraye in gozashtim ke age parametri ro nakhastim befrestim barash betone kole list ro bargardone
    #model2 :: q:Optional[str] = None
    #model3 :: q:Annotated[str | None , Query(max_length=50)] = None
    #har 3 ravesh yek khoroji ro namayesh midan
    if q :
        # TODO comper--> [operation iteration condition]
        return [item for item in names_list if item["name"] == q]

    return names_list





# @app.get("/names")
# def retrieve_names_list():
#     return names_list


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


@app.delete("/names/{name_id}")
def delete_name(name_id:int) :
    for item in names_list:
        if item["id"] == name_id:
            names_list.remove(item)
            return {"detail" : "object deleted successfully!"}
        
    return {"detail" : "object not found"}