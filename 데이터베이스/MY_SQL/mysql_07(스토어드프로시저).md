# 07_01 - 스토어드 프로시저
# 07_02 - 스토어드 함수와 커서
## 스토어드 함수란
* 스토어드 함수란 프로시저와 비슷하지만 직접 함수를 만들 때 사용하며, 반환 값을 필요로 한다.

* source
```
DELIMITER //
CREATE FUNCTION 스토어드_함수_명(매개변수)
    RETURNS 반환형식

BEGIN
    프로그래밍 코딩
    RETURNS 반환 값
END //
DELIMITER 

SELECT 스토어드 함수 이름 ();
```

* 사용시 설정
```
SET GLOBAL log_bin_trust_function_creators=1
```
* 예제

```
DELIMITER //
CREATE FUNCTION mysum(num1 INT ,num2 INT)
	RETURNS INT
BEGIN
	RETURN num1 + num2;
END //
DELIMITER ;

SELECT mysum(1,2);
```
## 커서란
* 테이블에서 한행 씩 처리기하기 위한 방식
> 커서 동작 방식
* 커서 선언
* 반복조건 선언
* 커서 열기
* 데이터 가져오기
* 데이터 처리하기
* 커서 닫기

> 8장 참고

# 07-03 - 트리거 
* 트리거란 테이블에 INSERT나 UPDATE,DELETE 작업 발생시 실행