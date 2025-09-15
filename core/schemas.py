from pydantic import BaseModel , field_validator , Field , field_serializer
#dar asl pydantic hamon naghshe serializers ro dar django ro dare 
#ma baraye validate kardan data az tarigh api az pydantic estefadeh mikonim va #! hata baraye response 

#! dar pydantic harchizi ke roye model vasle mishe (model_serializer) kol on model ro dar bar migire 
#! va har chizi ke roye field vasle mishe (field_serializer) kol on field ro dar bar migire

class BasePersonSchema(BaseModel):
    name : str = Field(... , description="Enter Persons name")
#mishe az in class ham baghie ersbari konan

#*Field(...) --> mandatory yani field ejbarie

    @field_validator("name" ,mode="after")
    def validate_name(cls , value: str):
        if len(value) > 32:
            raise ValueError("Name must not exceed 32 characters")
        if not value.isalpha():
            raise ValueError("Name must contain only alphabetic characters")
        return value

    @field_serializer("name")
    def serialize_name(value):
        return value.title()


class PersonCreateSchema(BasePersonSchema):
    name : str
    
    
class PersonResponseSchema(BasePersonSchema):
    id : int =Field(...,description="Unique user identifier")
    name : str
    
    
class PersonUpdateSchema(BasePersonSchema):
    name : str
