import MySQLdb

# Connect to the database
#db = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '',db = 'test')
#cursor = db.cursor()

# Create a table
#cursor.execute("Create table details (name varchar(100) , age int(5),location varchar(200))")

# Insert into the table
#cursor.execute("Insert into details values('Tony Stark',34,'New York')")
#cursor.execute("Insert into details values('Forster Okyere',24,'Kumasi')")

# Update the table
#cursor.execute("Update details set name = 'Ebenezer Offei Okyere ' where name = 'Ebenezer Offei'")

# Delete a query from the table
#cursor.execute("Delete from details where name = 'Selasi Kove'")

# Select from the table
#cursor.execute('Select * from details where like "%E"')
#print(cursor.fetchall())
#db.commit()
#db.close()

class MySQLite():
    """ This class helps users to use mysql easier and faster """
    def __init__(self,host = 'localhost',user = 'root',passwd = '',db = '',**kwargs):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        
        # Connect th the database
        try:
            self.mysql = MySQLdb.connect(host = self.host,user = self.user,passwd = self.passwd,db = self.db,**kwargs)
        except MySQLdb.DatabaseError:
            print('There is something wrong with the database')
        except MySQLdb.Error:
            print('A error was recorded')
        except MySQLdb.MySQLError:
            print('A mysql error has occured')
        except Exception:
            print("A general error")
    @staticmethod        
    def mysqlite_decorator(func,*args,**kwargs):        
        try:
            func(*args,**kwargs)
        except MySQLdb.DatabaseError:
            print('There is something wrong with the database')
        except MySQLdb.Error:
            print('A error was recorded')
        except MySQLdb.MySQLError:
            print('A mysql error has occured')
        except Exception:
            print("A general error")
        
        
    def insert(self,tablename,values):
        """ This method allows to insert a row into the database """
        self.mysqlite_decorator(self.insert_func,tablename,values)
        
    def insert_func(self,tablename,values):
        self.cursor = self.mysql.cursor()
        self.cursor.execute(f"Insert into {tablename} values({values})")
        self.mysql.commit()
        
    def insert_multiple(self,tablename,list_of_values):
        """ This method allows the user to insert multiple rows into the database """
        for i in list_of_values:
            self.mysqlite_decorator(self.insert_func,tablename,i)
        

list_of_values = [
    "'Ruth Okyere',13,'Koforidua'",
    "'Ebenezer Offei',20,'Dansoman'",
    "'Sackey Stephen',19,'Tafo'",
]

tuple_of_values = (
    "'Selasi Kove',18,'Nsawam'",
    "'Tony Stark',48,'New York'",
)
d = MySQLite(db = 'test')
d.insert_multiple('details',list_of_values)
d.insert_multiple('details',tuple_of_values)



