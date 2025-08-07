from pydantic import BaseModel
#dar asl pydantic hamon naghshe serializers ro dar django ro dare 
#ma baraye validate kardan data az tarigh api az pydantic estefadeh mikonim va #! hata baraye response 

class BasePersonSchema(BaseModel):
    name : str
#mishe az in class ham baghie ersbari konan

class PersonCreateSchema(BaseModel):
    name : str
    
    
class PersonResponseSchema(BaseModel):
    id : int
    name : str
    
    
class PersonUpdateSchema(BaseModel):
    name : str
