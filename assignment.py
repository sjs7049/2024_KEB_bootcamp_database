import pymysql

def high_orders():
    connection = pymysql.connect(
        host='localhost', user='root', passwd='worldcup7!',
        database = 'madang',port=3306, charset='utf8')
    
    try:
        with connection.cursor() as cursor:
            sql = """
            CREATE VIEW Highorders
            AS SELECT b.bookid '도서번호', b.bookname '도서이름', cs.name '고객이름', 
            b.publisher '출판사', od.saleprice '판매가격'
            FROM Book b, Customer cs, Orders od
            WHERE cs.custid=od.custid AND b.bookid=od.bookid AND od.saleprice = 20000;
            """
            cursor.execute(sql)
            
            result = "SELECT * FROM Highorders;"
            cursor.execute(result)
            data = cursor.fetchall()
            
            for rowdata in data:
                print('{0}\t{1:<}\t{2:<}\t{3:<}\t{4:<}'.format(
                    rowdata[0],rowdata[1],rowdata[2],rowdata[3],rowdata[4]))
            cursor.close()
    finally:
        connection.close()

if __name__ == "__main__":
    high_orders()