import random
from fastapi import FastAPI, File , Query ,status , HTTPException , Path , Form , Body , UploadFile 
from typing import List
from typing import Annotated ,Optional
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from dataclasses import dataclass
from schemas import PersonCreateSchema , PersonResponseSchema , PersonUpdateSchema
from typing import List
# import uvicorn

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("apllication startup")
    yield #miad aval print ro anjam mide baad mire donbal edameh barname va dobare moghe payane barname khat painisho chap mikone
    print("application shutdown")



app = FastAPI(lifespan=lifespan)


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




@app.get("/names" , response_model = List[PersonResponseSchema]) #zamani ke ye response model ba objective list darim bayad hatman az response model list estefaeh koinm , az [] estefadeh koinm
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


@app.get("/names/{name_id}" , response_model = PersonResponseSchema) #dar inja list nist chon darim detal daryaft mikonim 
def retrieve_name_detail(name_id:int = Path(title="object id ",description="the id of the name in names_list")):
    # vaghti ke ma mosavi(=) mizarim darim migim ke hoviate on chi hast
    for name in names_list:
        if name["id"] == name_id:
            return name
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="object not found")


@dataclass
class Student:
    name :str
    age:int
@dataclass
class StudentResponse:
    id:int
    name :str
    


@app.post("/names" , status_code=status.HTTP_201_CREATED , response_model=PersonResponseSchema)
# def create_name(name :str = Body(embed=True)):
# def create_name(student: Student):
def create_name(person:PersonCreateSchema):
    # agar az Body(embed=True) form estefadeh konim on vaght bayad be sorat jason befrestim , dar kol bishtar az Body estefadeh mishe nesbate be Form
    name_obj = {"id" : random.randint(6,101) , "name" : person.name}
    names_list.append(name_obj)
    
    return name_obj



@app.put("/names/{name_id}" , status_code=status.HTTP_200_OK , response_model =PersonResponseSchema)
def update_name_detail(person : PersonUpdateSchema , name_id:int =Path() ):
    for item in names_list:
        if item["id"] == name_id:
            item['name'] = person.name
            return item
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="object not found")


@app.delete("/names/{name_id}" )
def delete_name(name_id:int) :
    for item in names_list:
        if item["id"] == name_id:
            names_list.remove(item)
            return  JSONResponse(content={"detail" : "object removed successfully!"} , status_code=status.HTTP_200_OK) #agar 204 bashe be ma message ro neshon nmide
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="object not found")


# !yek ravesh baraye upload file
# @app.post("/upload_file/")
# async def upload_file(file: bytes=File()):
#     print(file)
#     return {"file_size" : len(file)}

@app.post("/upload_file/")
async def upload_file(file : UploadFile = File()):
    content = await file.read() 
    print(file.__dict__)
    return {"filename" : file.filename , "content_type" : file.content_type , "file_size" : len(content)}


@app.post("/upload-multiple/")
async def upload_multiple(files: List[UploadFile]):
    return [
        {"firstname" : file.filename , "content_type" : file.content_type}
        for file in files
    ]