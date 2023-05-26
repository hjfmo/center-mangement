

import sqlite3
class Database:
    def __init__(self,dp):        
        pass
        self.con = sqlite3.connect(dp)
        self.cur = self.con.cursor()
        sql= ""
        CREATE TABLE IF NOT EXISTS STUDENTS(
            id integer primary key,
            name text,
            age text,
            syear text,
            email text, 
            gender text,
            mobile text,
            address text,
            )
        """
        self.cur.execute(sql)
        self.con.commit()
        
        
        
        
        
def insert(self, name,age,syear,email,gender,mobile,address):
       self.cur.execute("insert into EMPLOYEES values(null,?,?,?,?,?,?,?)",
                        (name,age,syear,email,gender,mobile,address))
       self.con.commit()
        
        
        
        
        
        
          
def fetch(self, ):
    
                            self.cur.execute("SELECT * FROM EMPLOYEES")
                            rows = self.cur.fetchall()
                            return rows
        
                    
def remove(self):
    
        self.cur.execute("delete from EMPLOYEES where id =?",(id,))
        
        self.con.commit()
        
def update(self,id,name,syear,email,gender,mobile,address):
           self.cur.execute("update EMPLOYEES set name=?,age=?,syear=?,email=?,gender=?,mobile=?,address=?,where id=?",
            (name,age,job,email,gender,mobile,address,id))
           self.con.commit()
           
        
        
        
        
        
        
        
        
        
        
                        
                        
                        