# 오류
1. DELIMITER ; -> DELIMITER와 세미콜론은 반드시 띄워줘야 함
2. FULL OUTER SCAN은 mysql에서 사용하지 아니함
3. mysql 버전문제 - mac에서 Mysql 8.0.31,32와 workbench 8.0.31 8.0.32workbench는 SELECT문등 실행시 충돌 발생
4. mysql이 이미 있음에도 불구하고, brew를 통해 설치하면 설치 되니 유의 해야함(단, 이 경우 홈페이지를 통해 다운 받음)

# 기타 복사 붙여넣기용 코드
* MYSQL에서 스토어드 함수 사용시 설정
```
SET GLOBAL log_bin_trust_function_creators=1
```