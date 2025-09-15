from pydantic import BaseModel , field_validator
#dar asl pydantic hamon naghshe serializers ro dar django ro dare 
#ma baraye validate kardan data az tarigh api az pydantic estefadeh mikonim va #! hata baraye response 

class BasePersonSchema(BaseModel):
    name : str
#mishe az in class ham baghie ersbari konan

    @field_validator("name" ,mode="after")
    def validate_name(cls , value: str):
        if len(value) > 32:
            raise ValueError("Name must not exceed 32 characters")
        if not value.isalpha():
            raise ValueError("Name must contain only alphabetic characters")
        return value

    


class PersonCreateSchema(BasePersonSchema):
    name : str
    
    
class PersonResponseSchema(BasePersonSchema):
    id : int
    name : str
    
    
class PersonUpdateSchema(BasePersonSchema):
    name : str
