
from CustomerDAO import CustomerDAO

def main():
    dao = CustomerDAO("customers.db")
    customers = dao.find_all()

    for customer in customers:
        print(customer)

if __name__ == '__main__':
    main()