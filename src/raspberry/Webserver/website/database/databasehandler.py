import mysql.connector
import mysql
from mysql.connector import errorcode

class DatabaseHandler:
    def __init__(self):
        pass
    
    def isValid(self, uname, pwd):
        try:
            dbConn = self.databaseConnection()
            cursor = dbConn.cursor()
            
        except:
            result = 'Please contact system administrator, could not connect to database.'
            return result
        
        try:
            sqlQuery = "SELECT namn FROM Användare WHERE lösenord = '%s'" % (pwd)
            cursor.execute(sqlQuery)
            result = cursor.fetchall()
            
        except:
            result = 'Please contact system administrator, invalid query'
            return result
            
        if not result:
            result = 'false'
            return result
        
        else: 
            if result[0][0] == uname:
                result = uname
                    
        dbConn.close()
        return result
    
    def databaseConnection(self):
        try:
            cnx = mysql.connector.connect(user='root', password='banan123.', host='127.0.0.1', database='test')
            
        except:
            cnx = 'Could not connect to database.'
            
        return cnx