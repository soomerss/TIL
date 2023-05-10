# PostgreSQL 이자 Redshift를 위한 공간임

## DDL
> CREATE

CTAS : Create Table As Select -> Select 문을 통해 생성한 테이블을 다른 테이블로 생성하는 방법

> ALTER 

ALTER TABLE table_name ADD Column 필드이름 필드타입

ALTER TABLE table_name RENAME 현재필드이름 to 바꿀 필드이름

ALTER TABLE table_name DROP Column 필드이름

ALTER TABLE table_name RENAME to 바꿀 테이블이름

> DROP

DROP TABLE table_name , DROP TABLE IF EXISTS table_name

TRUNCATE table_name : 테이블 스키마(관계)는 남기게됨

DELETE FROM table_name where 조건 : 조건에 맞는 레코드 삭제!! (DML)

## 데이터 업무할 때 데이터 오류 점검사항
1. 중복되었는지 여부
   - 전체 열이 DISTINCT된 테이블에서 COUNT한것과 원래 테이블에서 COUNT한것의 차이를 보면됨

2. 값이 비었는지 여부
   - COUNT(CASE WHEN field IS NULL THEN 1 END) 반복 후 특정 필드가 0이상이면 NULL의 개수임)

3. primary key가 잘 지켜지고 있는지 여부
   - GROUP BY PRIMARY KEY FIELD 그리고 count하여 그 값이 1이상이면 안지켜지고 있는것임
  
4. 최근 데이터가 있는지 여부
   - max(날짜), mIN(날짜)
해당 순서로 데이터를 보더라도 1000~10000 row 정도는 살펴보면서 문제가 있는지 노가다가 필요함!

## WITH table명 AS
- WITH 임시테이블명 AS SELECT 를 하게 되면 그 후 하게 되는 작업을 해당 테이블명을 참고하여 진행할 수 있다. JOIN을 많이 할 경우 SQL구문이 생각보다 깔끔하지 않은데, 이 경우 매우 유용한 작업을 해준다.

## CTAS
- CREATE TABLE table명 AS SELECT~~ : 테이블 생성 시 해당 SELECT 구문대로 테이블이 생성되기 때문에 매우 편리하다
- 그리고 CREATE 시에 DROP TABLE IF EXISTS 테이블명을 하게 되면 오류를 방지한다.

## ALTER
ALTER TABLE table_name ADD COLUMN field_name field_type
ALTER TABLE table_name RENAME field_name TO field_name
ALTER TABLE table_name DROP COLUMN field_name
ALTER TABLE table_name RANATE TO table_name

## 오페레이터
필드명 :: type
그 외 CAST (필드 AS type)