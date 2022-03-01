
import pymysql

class DataBase:
            
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='abadon',
        db='webheroes',
        cursorclass=pymysql.cursors.DictCursor                
    )

    with connection:      
        with connection.cursor() as cursor:
            # Read a single record
            sql = 'SELECT * FROM wp_users'
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)        
            
        
database = DataBase()     
        
    