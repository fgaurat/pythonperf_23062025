from flask import Flask,render_template
from CustomerDAO import CustomerDAO
app = Flask(__name__)

# flask run
# flask run --debug
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def index():
    dao = CustomerDAO('customers.db')
    customers = dao.find_all()
    return render_template("customers.html",customers=customers,name="Fred")



# @app.route("/old")
# def old_index():
#     html="<table>"
#     dao = CustomerDAO('customers.db')
#     customers = dao.find_all()
#     for customer in customers:
#         html+=f"""<tr>
#         <td>{customer.id}</td>
#         <td>{customer.first_name}</td>
#         <td>{customer.last_name}</td>
#         <td>{customer.gender}</td>
#         <td>{customer.ip_address}</td>
#         </tr>"""
#     html+="</table>"
#     return html


