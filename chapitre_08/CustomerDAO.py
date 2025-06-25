import sqlite3


class CustomerDAO:
    

    def __init__(self,db_file) -> None:
        self.__con = sqlite3.connect(db_file)

    def find_all(self):
        customers = []
        sql="SELECT id,first_name,last_name,email,gender,ip_address FROM customers_tbl"
        cur = self.__con.cursor()
        rs = cur.execute(sql)

        for row in rs:
            print(row)

        return customers

    def __del__(self):
        self.__con.close()