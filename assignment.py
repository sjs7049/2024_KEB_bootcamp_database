import pymysql

def high_orders_alter():
    connection = pymysql.connect(
        host='localhost', user='root', passwd='worldcup7!',
        database = 'madang',port=3306, charset='utf8')
    
    try:
        with connection.cursor() as cursor:
            sql = """
            CREATE OR REPLACE VIEW Highorders
            AS SELECT b.bookid, b.bookname, cs.name, b.publisher
            FROM Book b, Customer cs, Orders od
            WHERE cs.custid=od.custid AND b.bookid=od.bookid AND od.saleprice = 20000;
            """
            cursor.execute(sql)
            
            result = "SELECT * FROM Highorders;"
            cursor.execute(result)
            data = cursor.fetchall()
            
            for rowdata in data:
                print('{0}\t{1:<}\t{2:<}\t{3:<}'.format(
                    rowdata[0],rowdata[1],rowdata[2],rowdata[3]))
            cursor.close()
    finally:
        connection.close()

if __name__ == "__main__":
    high_orders_alter()