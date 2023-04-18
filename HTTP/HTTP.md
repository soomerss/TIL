# HTTP

## 인터넷과 웹
- 인터넷은 컴퓨터 끼리 연결한 것이고, web은 인터넷상에서 정보를 교환하기 위한 시스템이다.

## 웹의 정보 교환
- 정보를 요청하는 클라이언트와 정보를 제공하는 서버로 구성
- 클라이언트가 서버에 작업수행 요청하고 서버가 작업을 수행
- 서버가 클라이언트에 응답
- 위 구조를 HTTP라고함
- Hyper TransFer Protocol - 웹 상에서 정보를 주고받기 위한 약속(protocol)
- Header에 받을 사람과 보내는 사람의 정보를 포함시켜 요청
- Body로 이루어진 내용이 전달
- 요청(request) - 응답(response)
- response의 header에는 Body의 타입 및 응답코드 등이 포함되어 응답 받을 수 있다.

## 웹 사이트와 웹 페이지
- 웹 속에 있는 문서 하나는 웹 페이지로 HTML 등의 코드로 구성되어 있음
- 웹 페이지의 모음은 웹 사이트
- 통상 웹 페이지는 웹 브라우저를 통해 특정 서버에 요청되고, 응답받음

## 파이썬과 HTTP 통신
- 기초 통신
```
import requests

res = requests.get(url)
print(res.header)
print(res.text)
```

## 참고 사이트 
https://webhook.site