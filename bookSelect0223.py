import pymysql

# 데이터베이스 접속 관련 변수들 초기화
host = "localhost"
port = 3306
database = "madang"
username = "root"
password = "worldcup7!"

# 접속 상태 확인
conflag = True

try:
    print("데이터베이스 연결 준비..")
    conn = pymysql.connect(host=host, user=username, passwd=password, 
                           db=database, port=port, charset='utf8')
    print("데이터베이스 연결 성공")
except Exception as err:
    print("데이터베이스 연결 실패")
    conflag=False


# 접속에 성공한다면 실행
if conflag == True:
    # 커서(cursor) 객체 생성
    cursor = conn.cursor()
    sqlString = 'select * from book;'
    res = cursor.execute(sqlString)
    data = cursor.fetchall()

    print("data의 타입=", type(data))
    print('{0}\t{1:<} \t{2:<} \t{3:<}'.format('BOOK NO','BOOKNAME','PUBLISHER','PRICE'))
    
    # 레코드들 출력
    for rowdata in data:
        print('{0}\t{1:<} \t{2:<} \t{3:<}'.format(rowdata[0],rowdata[1],rowdata[2],rowdata[3]))

cursor.close()
conn.close()