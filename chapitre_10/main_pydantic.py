

from pydantic import BaseModel,field_validator

class Customer(BaseModel):
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
    

def main():
    c = Customer(id=1,first_name="Fred",last_name="GAURAT",email="toto@truc.com",gender="Male",ip_address="12.12.12.12")
    print(c)

if __name__ == '__main__':
    main()