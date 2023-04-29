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
* 전화번호 데이터는 정수형이 적합한지 문자형이 적합한지에 대해서
* 정수형이란 계산할 필요가 있고, 대소의 구분이 의미가 있을때 정수형을 하는 것이 바람직하다.
* 따라서, 숫자이긴 하지만 주민등록번호, 우편번호, 전화번호 등은 문자형이 적합하다.
* 
# 04-02(조인)

## 내부조인
* A inner join B on 조건
* 조건에 맞는 쌍을 매칭한다.

## 외부조인
* A LEFT(RIGHT) JOIN B ON 조건
* 조건에 맞는 쌍을 매칭한다.
* A(또는 B)를 기준으로 B를 붙인다. B는 null데이터로 있을 것이다.

* FULL JOIN은 쌍을 매칭한다. A를 기준으로 붙이고, B를 기준으로 붙이는데, 'MYSQL'은 지원하지 않는다.
  
## 상호조인
* A Cross JOIN B
* ON 조건이 없다.
* a에서 전부를 B에서 전부를 그 수는 행 * 행이다.
* FROM A,B와 같다.

## 자체조인
* 별칭을 이용하여 하나의 테이블을 두개가 있는 것처럼 상호 조인 하는 방법을 말한다.

# 04-03 SQL 프로그래밍

```
DELIMITER //
CREATE PROCEDURE myproc()
BEGIN
    구문을 적는 곳
END //
DELIMITER ; -- DELIMITER 다음 ;를 꼭 띄워주자!!!!!
```

- DELIMITER는 구획의 시작과 끝이라는 뜻이다.
## 프로그래밍 제 방법

```
IF 조건 THEN
구문
ELSE 
구문
END IF;
```

```
포인트명:
WHILE 조건 DO
구문 LEAVE -- 종료
구문 ITERATE 포인트 -- CONTINUE
END WHILE
```
DECLARE 변수명 변수형식 -- 변수 선언
SET 변수명 = 값 -- 변수에 할당
SELECT f into 변수 -- f를 변수에 할당
PREPARE 구문명 from 'sql'; -- 준비 후 대기
EXECUTE 구문명 [USING 변수명]; -- 실행
DEALLOCATE PREPARE 구문명; -- 대기 해제
CALL 함수명 -- 함수호출 

CASE 
    WHEN(조건) then 값
    WHEN(조건) then 값
    WHEN(조건) then 값
END
-- select 문에 많이 쓰인다. 이때 다른 SELECT 문의 ALIAS를 조건에 넣지 말자. 오류난다.

## 날짜
CURRENT_DATE(): 오늘날짜
CURRENT_TIMESTAMP(): 오늘 날짜 및 시간
DATEDIFF(날짜,날짜) : 날짜와 날짜의 차이를 '일수'로 알려줌

