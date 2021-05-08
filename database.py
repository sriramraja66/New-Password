import sqlite3
from encdec import *

try:
    db=sqlite3.connect('data/data.db') 
    cur=db.cursor()
except:
    print("Creating Darabase ...")
    with open('data/data.db',"+w") as f:
        pass
    db=sqlite3.connect('data/data.db') 
    cur=db.cursor()



class database:
    def viewall(self):
        try:
            cur.execute("SELECT * FROM user")
        except:
            print("Creating Table...")
            sqlcommand = """
                CREATE TABLE user(
                    id INTEGER PRIMARY KEY,
                    description CHAR(50),
                    passwd CHAR(300)
                );"""
            cur.execute(sqlcommand)
            db.commit()
            cur.execute("SELECT * FROM user")
        lst = cur.fetchall()
        # print(lst)
        for i in lst:
            enc = i[2].encode()
            dec = decrypt(enc,load_key())
            print(f"Id : {i[0]}\tDescription : {i[1]}\tPassword : {dec}\n")
        
    def view(self,id):
        sqlcommand = "SELECT * FROM user WHERE id={id}".format(id=id)
        cur.execute(sqlcommand)
        lst = cur.fetchone()
        print(f"ID : {lst[0]}\nDescription : {lst[1]}\nPassword : {lst[2]}")

    def insert(self,dese,passwd,id = "NULL"):
        f_s = """
        INSERT INTO user(id,description,passwd) VALUES({id},"{dese}","{passwd}");
        """
        sqlcommand = f_s.format(dese=dese,passwd=passwd,id = id)
        cur.execute(sqlcommand)
        db.commit()  

    def delete(self,id):
        fs = """
        DELETE FROM user WHERE id = {id}
        """
        sqlcommand = fs.format(id=id)

        cur.execute(sqlcommand)
        db.commit()

    def update(self,id,passwd):
        f_s = """
        UPDATE user SET passwd = "{passwd}" WHERE id = {id}
        """.format(id = id,passwd=passwd)
        cur.execute(f_s)
        db.commit()

    def remove_db(self):
        cur.execute("DELETE FROM user;")
        db.commit()
        print("Data Erased..")


base = database()

if __name__ == '__main__':
    base.viewall()
    base.remove_db()