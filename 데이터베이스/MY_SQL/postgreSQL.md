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

## Join 하기 전 고려할 사항
one to one 관계 - 완전한 1:1도 있지만, 부분집합의 경우도 있다.
one to many 관계
many to one 관계 - left join 등을 할 때 유의해야 한다.
many to many 관계 - 잘 쓰이지는 않는다.

## join의 종류
inner join - 상호조건에 일치하는 레코드만을 연결한다. 
left join - 상호조건에 일치하는 레코드만을 연결하고, 왼쪽에 위치한 테이블은 모두 출력하는데, 이때 오른족에 위치한 테이블의 값들은 null로 표시한다. 
right join - 상호 조건에 일치하는 레코드만을 연결하고 , 오른쪽에 위치한 테이블은 모두 출력하는데, 이때 왼쪽에 위치한 테이블의 값들은 null로 표시한다. 사실상 left join과는 테이블의 위치만 바꾸면 되는 문제라 둘 중 하나만 쓰게 된다고 한다.
full join - 상호조건에 일치하는 레코드만을 연결하고, 왼쪽테이블의 값과 오른쪽테이블의 값을 NULL로, 오른쪽테이블의 값과 왼쪽테이블의 값을 NULL로 표시한다.
cross join(cartesian join) - 왼쪽 레코드 * 오른쪽 레코드, 즉 모든 경우의 수를 나타낸다.
self join - 테이블 자기 자신을 별칭으로 구분하여 조인하는 방식이다.

## 3개의 join
from a 
inner join b on ~
left join C on ~ 
-> 먼저 a 와 b 를 inner join 하고, 해당 테이블과 C를 left join한다.

## Boolean type
아래의 둘은 같은 표현이다.
field is TRUE
field = TRUE

아래의 둘은 다른 표현이다.
field is not FALSE
field is TRUE

이유는 Boolean Type이 True, False, Null로 이루어져 있기 때문이다.

## null
Null은 가로 연산시 NULL이다. 
* NULLIF(인자1, 인자2) - 인자1을 리턴한다. 단, 인자1의 값이 인자2와 같을 때는 Null을 리턴한다.
0으로 나누는 나누기 연산시 오류를 NULLIF 함수로 해결하는 방법
3/NULL -> NULL
3/0 -> 오류
a / NULLIF(b,0) -> b라는 필드의 값이 0과 같다면, 0이 아니라 NULL로 처리하게 한다.
* COALESCE(인자1,인자2,인자N) -> 인자를 하나씩 넣어 NULL이 아니라면 그 값을 리턴하고, NULL이라면 그 다음 인자를 넣어 같은 방식으로 진행한다. 만약 N번의 인자까지 NULL이 나온다면 최종 값은 NULL을 리턴한다.
* 해당 함수의 활용은 COALESCE(field, 0) : 필드의 값이 NULL이라면 두번째 인자인 상수값 0을 리턴한다. 0은 언제나 NULL이 아니기 때문에 이렇게 활용하게 된다면 NULL이 나오는 경우 언제나 0을 리턴한다. 

## 공백이나 예약어를 사용한 필드이름을 사용하려면?
""를 사용하자, 단, ""를 사용하여 필드이름을 지정했다면 나중에 사용시에도 ""를 사용해야 한다.

## CTAS
CTAS로 테이블을 생성하여 값을 저장할 때 ORDER BY 적용하여 저장할 필요는 없다. 어차피 시스템에서 알아서 그 순서를 조정하여 등록하기 때문이다.

## WINDOW 함수
ROW_NUMBER() OVER(PARTIRION BY ~~~ ORDER BY ~~~ ROWS/RANGE ~~~)
window함수는 rank(),sum() 등 다양하다. SUM()은 필드를 인자로 가지지만, ROW_NUMBER()는 인자를 가지지 않는다.
PARTITION BY는 필드로 구역을 나누겠다는 의미이며, ORDER BY는 그 구역에서 특정필드로 순서를 매기며, 그 범위는 ROWS나 RANGE로 표현한다.
범위 표현에는 UNBOUNDED PRECEDING, 1 PRECEDING, CURRENT_ROWS, 1 FOLLOWING, UNBOUNDED FOLLOWING 등이 있으며, 가장 위, 1개 이전, 현재행, 1개 이후, 파티션에서 가장 끝 이라는 의미로 사용될 수 있다.
만약 ROWS UNBOUNDED PRECEDING은 파티션에서 가장 위 '행'부터 현재 행까지 범위로 잡는다. RANGE UNBOUNDE PRECEDING은 현재 '값' 보다 작은 '값'을 가진 부분을 범위로 잡는다.