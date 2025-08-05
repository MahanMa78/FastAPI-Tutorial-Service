from fastapi import FastAPI , Query ,status , HTTPException , Path , Form , Body
# import uvicorn
from typing import Annotated ,Optional
from fastapi.responses import JSONResponse
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
    content = {"message" : "Hello, World!"}
    return JSONResponse(content=content , status_code=status.HTTP_202_ACCEPTED)


# *
# if __name__ == "__main__":
#     uvicorn.run( "main.app" , host="0.0.0.0" , port = "8000" , reload=True )
# * for running the server : uvicorn main.app --reload --host 0.0.0.0 --port 8000




@app.get("/names")
def retrieve_names_list(q:str | None = Query(deprecated=True, alias="search",description="it will be searched with the title you provided",example="mahan", default=None , max_length=50)): 
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
def retrieve_name_detail(name_id:int = Path(alias="object id",title="object id ",description="the id of the name in names_list")):
    # vaghti ke ma mosavi(=) mizarim darim migim ke hoviate on chi hast
    for name in names_list:
        if name["id"] == name_id:
            return name
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="object not found")


@app.post("/names" , status_code=status.HTTP_201_CREATED)
def create_name(name:str = Body(embed=True)):
    # agar az Body(embed=True) form estefadeh konim on vaght bayad be sorat jason befrestim , dar kol bishtar az Body estefadeh mishe nesbate be Form
    name_obj = {"id" : random.randint(6,101) , "name" : name}
    names_list.append(name_obj)
    
    return name_obj



@app.put("/names/{name_id}" , status_code=status.HTTP_200_OK)
def update_name_detail(name_id:int =Path() , name:str = Form()):
    for item in names_list:
        if item["id"] == name_id:
            item['name'] = name
            return item
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="object not found")


@app.delete("/names/{name_id}" )
def delete_name(name_id:int) :
    for item in names_list:
        if item["id"] == name_id:
            names_list.remove(item)
            return  JSONResponse(content={"detail" : "object removed successfully!"} , status_code=status.HTTP_200_OK) #agar 204 bashe be ma message ro neshon nmide
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="object not found")