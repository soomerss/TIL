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

