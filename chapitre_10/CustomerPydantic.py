from pydantic import BaseModel,field_validator

class CustomerPydantic(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    gender:str
    ip_address:str

    @field_validator('email')
    def validate_email(cls,v):
        if '@' not in v:
            raise ValueError("Email error")
        return v
    