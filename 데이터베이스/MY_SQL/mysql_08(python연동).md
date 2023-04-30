# 08. pymysql을 이용하여 mysql연결


## python 코드 흐름
1. mysql에서 DB 생성
2. 연결자를 통해 DB로 연결
3. DB의 커서를 통해 SQL문을 주고 받음
4. 커서를 통해 테이블 생성-커밋 및 조회
5. 연결자 닫기

## 코드를 통해 테이블 생성 및 값 입력하기하기
```SQL
CREATE DATABASE db_ex; -- DB생성해주기
```
```python
import pymysql

conn = pymysql.connect(host='127.0.0.1',user='',password='',db='생성한 db',charset='utf8') # DB에 연결
cur = conn.cursor() # cursor(SQL구문 입.출력 통로)

# SQL구문 - 생성
sql = 'CREATE TABLE ex_table (id int AUTO_INCREMENT,name char(10), email char(20), addr char(20))' # 테이블 생성
# SQL구문 - 데이터 입력
# insert_sql = 'INSERT INTO ex_table VALUES (~~~~~~~~~)'
cur.execute(sql) # SQL 구문 실행

cur.commit() # 반영하기

conn.close() # 연결 끊기
```

## 코드를 통해 조회하기
* 데이터가 입력되었다고 가정한다.
```python
import pymysql

conn = pymysql.connect(host='127.0.0.1',user='',password='',db='생성한 db',charset='utf8') # DB에 연결
cur = conn.cursor() # cursor(SQL구문 입.출력 통로)

# SQL구문 - 생성
sql = 'SELECT * FROM ex_table;' # 테이블 조회 구문

cur.execute(sql) # SQL 구문 실행

a = cur.fetchall()  # 튜플형태로 레코드 전체가 반환됌
b = cur.fetchmany(4)  # 튜플형태로 레코드 4개가 반환됌
c = cur.fetchone()  # 튜플형태로 레코드 한개가 반환됌

print(a[:5])

# cur.commit() - 조회는 커밋할 필요가 없음

conn.close() # 연결 끊기
```

