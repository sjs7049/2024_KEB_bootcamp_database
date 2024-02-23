import pymysql

def high_orders_Output():
    connection = pymysql.connect(
        host='localhost', user='root', passwd='worldcup7!',
        database = 'madang',port=3306, charset='utf8')
    
    try:
        with connection.cursor() as cursor:
            sql = "SELECT bookname, name FROM Highorders;"
            cursor.execute(sql)
            data = cursor.fetchall()
            
            for rowdata in data:
                print('{0}\t{1:<}'.format(rowdata[0],rowdata[1]))
            cursor.close()
    finally:
        connection.close()

if __name__ == "__main__":
    high_orders_Output()