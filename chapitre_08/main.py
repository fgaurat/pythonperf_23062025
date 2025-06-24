import csv
import sqlite3

def main():
    with sqlite3.connect("customers.db") as con:
        cur = con.cursor()
        sql_insert="INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) VALUES(?,?,?,?,?)"
        # context manager
        with open('MOCK_DATA.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                del row['id']
                cur.execute(sql_insert,list(row.values()))

if __name__ == '__main__':
    main()