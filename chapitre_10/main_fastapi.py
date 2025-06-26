from fastapi import FastAPI
from CustomerPydantic import CustomerPydantic
app = FastAPI()


# fastapi run main_fastapi.py 
# fastapi run main_fastapi.py --reload
@app.get("/")
def hello_world():
    return {'hello':'world'}


# GET /customers => find_all
# GET /customers/1 => find_by_id(1)
# DELETE /customers/1 => delete(1)

# GET /customers/1 => find_by_id(1)
@app.get("/customers/{customer_id}")
def get_customer(customer_id:int)->CustomerPydantic:
    c = CustomerPydantic(id=customer_id,last_name="MARTIN",first_name="Jean",gender="Male",ip_address="0.0.0.0",email="toto@truc.com")
    return c







