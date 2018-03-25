import sqlite3

def db_connect():
    global conn
    conn = sqlite3.connect("AxisBank.sqlite")
    return(conn)

class DBHelper:

    def __init__(self, dbname="AxisBank.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
        print("Connection Successful with DB")
        self.conn.close()

    def setup(self):
        conn = db_connect()
        tblstmt = "CREATE TABLE IF NOT EXISTS account_details (cust_fname varchar(50), cust_lname varchar(50)," \
                  "cust_email varchar(50), cust_mobilnumber varchar(50), cust_accnum varchar(50), cust_atmnumber varchar(50)," \
                  "cust_atmpin varchar(50), cust_acccif varchar(50), cust_accifsc varchar(50), cust_accactivationcode varchar(50))"

        tblstmt4 = "INSERT INTO account_details  (cust_fname,cust_lname,cust_email, cust_mobilnumber,cust_accnum," \
                   "cust_atmnumber,cust_atmpin,cust_acccif,cust_accifsc,cust_accactivationcode) " \
                   "VALUES ('Rukhshan','Rahman','rukshanurrahman@gmail.com','8884300686','12345678','12345678'," \
                   "'1234','12345678','1234','12345678')"
        conn.execute(tblstmt)
        #conn.execute(tblstmt4)
        conn.commit()

    def check_details(self, dataToQuery):
        print(dataToQuery)
        conn = db_connect()
        stmt = "select * from account_details where cust_fname=(?) and cust_atmnumber=(?) and cust_atmpin=(?) and cust_accactivationcode=(?)"
        args = (dataToQuery[0],dataToQuery[5],dataToQuery[6],dataToQuery[9])

        result = [x for x in conn.execute(stmt, args)]
        return(result)
        conn.commit()
        #conn.close()