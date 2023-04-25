# 3-3 데이터 변경을 위한 SQL

## 데이터 입력 - INSERT
* INSERT INTO table명 [(열이름)] values(값)
* INSERT INTO table명 values(값)
* INSERT INTO table명 values (값),(값),(값)
* INSERT INTO table명 select * from ex
* 데이터 입력은 테이블의 열의 이름을 순서에 상관없이 나열한 후 값을 적는다. 열의 이름은 생략해도 무방하나 일단 적었다면
* 반드시 값의 개수도 일치해야한다. 여러 개의 값들을 입력하고 싶을 때에는 ,로 구분하여 나열한다.
* 다른 테이블의 데이터를 한번에 입력하고 싶을 때에는 values 자리에 select문을 쓸 수 있다.

### Auto_INCREMENT
* 값의 형식 중 자동으로 증가하는 AUTO_INCREMENT가 있다. 
* INSERT 시 NULL취급, 반드시 PRIMARY KEY 지정
* 처음이나 특정시점에 변경하고 싶을때에는 ALTER TABLE AUTO_INCREMENT = 시작값
* 단위를 변경하고 싶을때에는 시스템 변수 설정 SET @@auto_increment_increment = 증가값;
* 현재 어디까지 AUTO_INCREMENT가 진행되었는지 보는 법은 SELECT LAST_INSERT_ID();

### 참고사항
* 참고로 시스템 변수를 보고 싶을떄에는 select @@시스템변수;, 시스템변수 전체를 보고싶을때에는 show global variables;
* DESC TABLE > 테이블의 스키마를 볼 수 있다.

## 데이터 변경 - update
* update table명 set 열=값[,열2=값2,열3=값3] where 조건;
* 특정 행(조건으로 추출된)의 열값을 변경한다.
* Mysql_설정을 최초에 변경해야 구문이 작동한다.
* where 절을 작성하지 아니하면 전체열의 값이 변경되니 """주의"""
* 전체 열을 변경하는 경우란 전체 열에 특정 값을 곱하는 경우나 더하는 경우를 생각해볼 수 있다.

## 데이터 삭제 - DELETE
* DELETE FROM 테이블명 where 조건;
* 테이블의 특정조건을 만족하는 행을 삭제, 조건이 없다면 전체 행을 삭제하고 테이블은 남긴다.
* DROP TABLE명;
* TRUNCATE TABLE명;
* drop은 테이블을 남기지 않는다. TRUNCATE는 테이블 자체는 남긴다.
* 따라서 전체 대량의 데이터는 위 둘 중에 사용해야 시간적으로 효율이 높다.

# 4-1 데이터 형식

## 정수
* TINYINT, SMALLINT, INT,BIGINT
* 뒤에 unsigned(부호가 없는) 예약어를 붙이면 양의 정수의 범위로 사용할 수 있음
* ex) TINYINT(-127~127) > TINYINT UNSIGNED(0~255)

## 문자
* char(크기) - 불변, varchar(크기)-가변
* char는 실제데이터와 상관없이 크기를 차지하는 반면에 varchar의 경우 실제 데이터가 크기보다 작은 경우 해당 크기만큼 차지한다.
* 따라서 공간 활용도 측면에서는 VARCHAR가 우위이다. 다만, CHAR가 속도측면에서 우수하다.

## 대량의 데이터
* text, longtext, blob, longblob
* text는 대본 등의 저장, blob은 바이너리데이터(동영상 등) 저장
* long은 약 42억바이트를, 그렇지 아니한 경우 65535의 바이트를 가진다.

## 실수
* 소수점 7자리 float, 15자리 double


## 날짜와 시간
* 날짜 date
* 시간 time
* 날짜시간 datetime
* [(yyyy-mm-dd) (HH:mm:ss)]

## 변수
* set @변수명 = 값;

## limit과 변수
* limit에는 변수를 사용할 수 없지만 prepare, execute를 통해 실행 가능
* prepare 이름 from 'select * from tb_grade limit ?';
* execute 이름 using @변수
* ?는 나중에 변수 대입을 기다릴 자리를 의미한다.

## 데이터 형변환
* cast(값 as 형식)
* convert(값, 형식)
* 형식에는 SIGNED -> SIGNED INTEGER, UNSIGNED -> UNSIGNED INTEGER 등이 올 수 있다.
* 이를 명시적 형변환 이라고 하며, 시스템이 자동으로 형변환해주는 것을 암시적 형변환이라고 한다.
* 암시적 형변환의 예는 '1' + '2' 처럼 문자열은 +를 작동할 수 없어서 둘의 형을 정수로 변환후 더해주는 경우를 말한다.

### 참고사항
* 전화번호는 정수형이 적합한지 문자형이 적합한지에 대해서
* 정수형이란 계산할 필요가 있고, 대소의 구분이 의미가 있을때 정수형을 하는 것이 바람직하다.
* 따라서, 숫자이긴 하지만 주민등록번호, 우편번호, 전화번호 등은 문자형이 적합하다.